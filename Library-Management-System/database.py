import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "library.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    connection = get_connection()
    try:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT,
                isbn TEXT UNIQUE,
                quantity INTEGER NOT NULL,
                available INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                course TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                issue_date TEXT NOT NULL,
                return_date TEXT,
                status TEXT NOT NULL DEFAULT 'Issued',
                FOREIGN KEY(book_id) REFERENCES books(id),
                FOREIGN KEY(student_id) REFERENCES students(id)
            );
            """
        )

        connection.execute(
            "INSERT OR IGNORE INTO books (title, author, category, isbn, quantity, available) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Python Crash Course", "Eric Matthes", "Programming", "9781593279288", 5, 5),
        )
        connection.execute(
            "INSERT OR IGNORE INTO books (title, author, category, isbn, quantity, available) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Let Us C", "Yashavant Kanetkar", "Programming", "9788176566210", 4, 4),
        )
        connection.execute(
            "INSERT OR IGNORE INTO books (title, author, category, isbn, quantity, available) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Clean Code", "Robert C. Martin", "Software Engineering", "9780132350884", 3, 3),
        )
        connection.execute(
            "INSERT OR IGNORE INTO books (title, author, category, isbn, quantity, available) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Data Science from Scratch", "Joel Grus", "Data Science", "9781492041139", 3, 3),
        )
        connection.execute(
            "INSERT OR IGNORE INTO books (title, author, category, isbn, quantity, available) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Introduction to Algorithms", "Thomas H. Cormen", "Algorithms", "9780262046305", 2, 2),
        )

        connection.execute(
            "INSERT OR IGNORE INTO students (name, email, phone, course) "
            "VALUES (?, ?, ?, ?)",
            ("Aarav Sharma", "aarav@example.com", "9876543210", "B.Tech Computer Science"),
        )
        connection.execute(
            "INSERT OR IGNORE INTO students (name, email, phone, course) "
            "VALUES (?, ?, ?, ?)",
            ("Diya Patel", "diya@example.com", "9876501234", "BCA"),
        )
        connection.execute(
            "INSERT OR IGNORE INTO students (name, email, phone, course) "
            "VALUES (?, ?, ?, ?)",
            ("Kabir Singh", "kabir@example.com", "9123456780", "MCA"),
        )
        connection.commit()
    finally:
        connection.close()
