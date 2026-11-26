# Viva Questions and Answers

1. **What is this project?** It is a web-based system for managing books, students, issues, and returns.
2. **Which Python framework is used?** Flask.
3. **What is Flask?** A lightweight Python web framework.
4. **What database is used?** SQLite.
5. **Why use SQLite?** It is built into Python and needs little setup for a small application.
6. **What is sqlite3?** Python's standard library module for SQLite databases.
7. **What is a primary key?** A unique identifier for each row.
8. **What is a foreign key?** A column that connects a row to a primary key in another table.
9. **How are books and issues connected?** `issues.book_id` references `books.id`.
10. **How are students and issues connected?** `issues.student_id` references `students.id`.
11. **What is CRUD?** Create, read, update, and delete.
12. **What route shows the dashboard?** `GET /`.
13. **What does `render_template` do?** It displays an HTML template and passes data to it.
14. **What is Jinja2?** Flask's template engine for dynamic HTML.
15. **What is request.form?** It contains submitted form values.
16. **What is redirect?** It sends the browser to another route.
17. **What is url_for?** It generates a URL from a route function name.
18. **What are flash messages?** Temporary success or error notifications.
19. **How does the app prevent SQL injection?** It uses parameterized SQL queries.
20. **What happens while issuing a book?** A transaction is added and available quantity decreases.
21. **What happens while returning a book?** The issue status becomes Returned and available quantity increases.
22. **How are duplicate returns prevented?** Only issued transactions can be processed for return.
23. **Why cannot a used book be deleted?** It would remove the connection or history of an existing issue.
24. **What is a database transaction?** A group of operations that succeeds or fails together.
25. **What is `commit()`?** It permanently saves a successful transaction.
26. **What is `rollback()`?** It cancels changes from a failed transaction.
27. **What does foreign-key enforcement do?** It prevents invalid relationships.
28. **How is duplicate ISBN handled?** The database's unique constraint and an IntegrityError handler.
29. **How is duplicate student email handled?** The email column is unique and validated in the route.
30. **How are negative quantities prevented?** Backend validation rejects quantities below zero.
31. **What is HTML used for?** Defining the structure and forms of each page.
32. **What is CSS used for?** Styling, spacing, layout, colors, and responsiveness.
33. **How does search work?** The route reads a search value and uses SQL `LIKE` expressions.
34. **What could be improved in the future?** Authentication, roles, due dates, fines, reports, notifications, and PDF export.
