from datetime import date

import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for

from database import get_connection, init_db


app = Flask(__name__)
app.secret_key = "library-management-local-session-key"
init_db()


def clean(value):
    return value.strip() if value else ""


@app.route("/")
def dashboard():
    connection = get_connection()
    try:
        stats = {
            "total_books": connection.execute("SELECT COUNT(*) FROM books").fetchone()[0],
            "available_copies": connection.execute("SELECT COALESCE(SUM(available), 0) FROM books").fetchone()[0],
            "total_students": connection.execute("SELECT COUNT(*) FROM students").fetchone()[0],
            "issued_books": connection.execute(
                "SELECT COUNT(*) FROM issues WHERE status = 'Issued'"
            ).fetchone()[0],
        }
        recent_books = connection.execute(
            "SELECT * FROM books ORDER BY id DESC LIMIT 5"
        ).fetchall()
        recent_issues = connection.execute(
            """
            SELECT issues.*, books.title AS book_title, students.name AS student_name
            FROM issues
            JOIN books ON books.id = issues.book_id
            JOIN students ON students.id = issues.student_id
            ORDER BY issues.id DESC
            LIMIT 5
            """
        ).fetchall()
        return render_template(
            "dashboard.html",
            stats=stats,
            recent_books=recent_books,
            recent_issues=recent_issues,
        )
    finally:
        connection.close()


@app.route("/books")
def books():
    search = clean(request.args.get("search"))
    connection = get_connection()
    try:
        if search:
            rows = connection.execute(
                "SELECT * FROM books "
                "WHERE title LIKE ? OR author LIKE ? OR category LIKE ? "
                "ORDER BY id DESC",
                (f"%{search}%", f"%{search}%", f"%{search}%"),
            ).fetchall()
        else:
            rows = connection.execute("SELECT * FROM books ORDER BY id DESC").fetchall()
        return render_template("books.html", books=rows, search=search)
    finally:
        connection.close()


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = clean(request.form.get("title"))
        author = clean(request.form.get("author"))
        category = clean(request.form.get("category"))
        isbn = clean(request.form.get("isbn"))
        quantity_text = clean(request.form.get("quantity"))

        if not title or not author or not quantity_text:
            flash("Title, author, and quantity are required.", "error")
        else:
            try:
                quantity = int(quantity_text)
                if quantity < 0:
                    flash("Quantity cannot be negative.", "error")
                else:
                    connection = get_connection()
                    try:
                        connection.execute(
                            "INSERT INTO books (title, author, category, isbn, quantity, available) "
                            "VALUES (?, ?, ?, ?, ?, ?)",
                            (title, author, category, isbn or None, quantity, quantity),
                        )
                        connection.commit()
                        flash("Book added successfully.", "success")
                        return redirect(url_for("books"))
                    except sqlite3.IntegrityError:
                        flash("A book with this ISBN already exists.", "error")
                    finally:
                        connection.close()
            except ValueError:
                flash("Quantity must be a valid whole number.", "error")

    return render_template("add_book.html")


@app.route("/edit-book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    connection = get_connection()
    try:
        book = connection.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
        if book is None:
            flash("Book record not found.", "error")
            return redirect(url_for("books"))

        if request.method == "POST":
            title = clean(request.form.get("title"))
            author = clean(request.form.get("author"))
            category = clean(request.form.get("category"))
            isbn = clean(request.form.get("isbn"))
            quantity_text = clean(request.form.get("quantity"))

            if not title or not author or not quantity_text:
                flash("Title, author, and quantity are required.", "error")
            else:
                try:
                    new_quantity = int(quantity_text)
                    if new_quantity < 0:
                        flash("Quantity cannot be negative.", "error")
                    else:
                        issued_count = connection.execute(
                            "SELECT COUNT(*) FROM issues WHERE book_id = ? AND status = 'Issued'",
                            (book_id,),
                        ).fetchone()[0]
                        if new_quantity < issued_count:
                            flash(
                                f"Quantity cannot be lower than the {issued_count} currently issued copies.",
                                "error",
                            )
                        else:
                            available = new_quantity - issued_count
                            try:
                                connection.execute(
                                    "UPDATE books SET title=?, author=?, category=?, isbn=?, "
                                    "quantity=?, available=? WHERE id=?",
                                    (title, author, category, isbn or None, new_quantity, available, book_id),
                                )
                                connection.commit()
                                flash("Book updated successfully.", "success")
                                return redirect(url_for("books"))
                            except sqlite3.IntegrityError:
                                flash("A book with this ISBN already exists.", "error")
                except ValueError:
                    flash("Quantity must be a valid whole number.", "error")

        return render_template("edit_book.html", book=book)
    finally:
        connection.close()


@app.route("/delete-book/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    connection = get_connection()
    try:
        history = connection.execute(
            "SELECT COUNT(*) FROM issues WHERE book_id = ?", (book_id,)
        ).fetchone()[0]
        if history:
            flash("This book cannot be deleted because it has issue history.", "error")
            return redirect(url_for("books"))

        result = connection.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        if result.rowcount:
            flash("Book deleted successfully.", "success")
        else:
            flash("Book record not found.", "error")
        return redirect(url_for("books"))
    except sqlite3.Error as error:
        connection.rollback()
        flash(f"Unable to delete the book: {error}", "error")
        return redirect(url_for("books"))
    finally:
        connection.close()


@app.route("/students")
def students():
    search = clean(request.args.get("search"))
    connection = get_connection()
    try:
        if search:
            rows = connection.execute(
                "SELECT * FROM students "
                "WHERE name LIKE ? OR email LIKE ? OR course LIKE ? "
                "ORDER BY id DESC",
                (f"%{search}%", f"%{search}%", f"%{search}%"),
            ).fetchall()
        else:
            rows = connection.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
        return render_template("students.html", students=rows, search=search)
    finally:
        connection.close()


@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = clean(request.form.get("name"))
        email = clean(request.form.get("email")).lower()
        phone = clean(request.form.get("phone"))
        course = clean(request.form.get("course"))

        if not name or not email or not course:
            flash("Name, email, and course are required.", "error")
        elif "@" not in email or "." not in email:
            flash("Enter a valid email address.", "error")
        else:
            connection = get_connection()
            try:
                connection.execute(
                    "INSERT INTO students (name, email, phone, course) VALUES (?, ?, ?, ?)",
                    (name, email, phone, course),
                )
                connection.commit()
                flash("Student added successfully.", "success")
                return redirect(url_for("students"))
            except sqlite3.IntegrityError:
                flash("A student with this email already exists.", "error")
            finally:
                connection.close()

    return render_template("add_student.html")


@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():
    connection = get_connection()
    try:
        if request.method == "POST":
            student_id_text = clean(request.form.get("student_id"))
            book_id_text = clean(request.form.get("book_id"))
            issue_date = clean(request.form.get("issue_date")) or date.today().isoformat()

            if not student_id_text or not book_id_text:
                flash("Select both a student and a book.", "error")
            else:
                try:
                    student_id = int(student_id_text)
                    book_id = int(book_id_text)
                    connection.execute("BEGIN")
                    book = connection.execute(
                        "SELECT * FROM books WHERE id = ?", (book_id,)
                    ).fetchone()
                    student = connection.execute(
                        "SELECT * FROM students WHERE id = ?", (student_id,)
                    ).fetchone()

                    if book is None or student is None:
                        flash("The selected student or book no longer exists.", "error")
                    elif book["available"] <= 0:
                        flash("This book has no available copies.", "error")
                    else:
                        connection.execute(
                            "INSERT INTO issues (book_id, student_id, issue_date, status) "
                            "VALUES (?, ?, ?, 'Issued')",
                            (book_id, student_id, issue_date),
                        )
                        connection.execute(
                            "UPDATE books SET available = available - 1 WHERE id = ?",
                            (book_id,),
                        )
                        connection.commit()
                        flash("Book issued successfully.", "success")
                        return redirect(url_for("issued_books"))
                except (ValueError, sqlite3.Error) as error:
                    connection.rollback()
                    if isinstance(error, sqlite3.Error):
                        flash(f"Unable to issue the book: {error}", "error")
                    else:
                        flash("Invalid selection.", "error")

        students_rows = connection.execute(
            "SELECT * FROM students ORDER BY name"
        ).fetchall()
        books_rows = connection.execute(
            "SELECT * FROM books WHERE available > 0 ORDER BY title"
        ).fetchall()
        return render_template(
            "issue_book.html",
            students=students_rows,
            books=books_rows,
            today=date.today().isoformat(),
        )
    finally:
        connection.close()


@app.route("/issued-books")
def issued_books():
    status = clean(request.args.get("status"))
    connection = get_connection()
    try:
        query = """
            SELECT issues.*, books.title AS book_title, students.name AS student_name,
                   students.email AS student_email
            FROM issues
            JOIN books ON books.id = issues.book_id
            JOIN students ON students.id = issues.student_id
        """
        parameters = ()
        if status in ("Issued", "Returned"):
            query += " WHERE issues.status = ?"
            parameters = (status,)
        query += " ORDER BY issues.id DESC"
        rows = connection.execute(query, parameters).fetchall()
        return render_template("issued_books.html", issues=rows, status=status)
    finally:
        connection.close()


@app.route("/return-book/<int:issue_id>", methods=["POST"])
def return_book(issue_id):
    connection = get_connection()
    try:
        connection.execute("BEGIN")
        issue = connection.execute(
            "SELECT * FROM issues WHERE id = ?", (issue_id,)
        ).fetchone()

        if issue is None:
            flash("Issue record not found.", "error")
        elif issue["status"] == "Returned":
            flash("This book has already been returned.", "error")
        else:
            connection.execute(
                "UPDATE issues SET status='Returned', return_date=? WHERE id=?",
                (date.today().isoformat(), issue_id),
            )
            connection.execute(
                "UPDATE books SET available = available + 1 WHERE id=?",
                (issue["book_id"],),
            )
            connection.commit()
            flash("Book returned successfully.", "success")
            return redirect(url_for("issued_books"))
        connection.commit()
    except sqlite3.Error as error:
        connection.rollback()
        flash(f"Unable to return the book: {error}", "error")
    finally:
        connection.close()
    return redirect(url_for("issued_books"))


if __name__ == "__main__":
    app.run(debug=True)
