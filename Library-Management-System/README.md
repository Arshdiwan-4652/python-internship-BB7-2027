# Library Management System

A professional, responsive web application for managing a small library.

## Introduction

This project allows librarians to manage books and students, issue books to students, and record returns. It is built as a beginner-friendly full-stack Python application with Flask and SQLite.

## Objectives

- Digitize basic library records.
- Track available and issued book copies accurately.
- Prevent duplicate or invalid transactions.
- Provide a clean dashboard and searchable management screens.

## Features

- Dashboard statistics and recent activity.
- Book add, view, search, edit, and eligible deletion.
- Student add, view, and search.
- Book issue and return workflows.
- Issued and returned history.
- Backend validation and SQLite transactions.
- Responsive dark-navy and white interface.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- SQLite3

## Folder Structure

```text
Library-Management-System/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── library.db
├── templates/
└── static/
```

## Database Design

- `books`: stores book details, total quantity, and available copies.
- `students`: stores student name, unique email, phone, and course.
- `issues`: stores issue and return history with foreign keys to books and students.

Foreign-key enforcement is enabled for database connections. Issue and return operations use explicit transactions.

## Installation

1. Open a terminal in this project folder.
2. Create a virtual environment:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the Application

```powershell
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

The database and sample records are initialized automatically the first time the application starts.

## Screenshots

Add dashboard, books, issue, and return screenshots here after running the application.

## Testing

Test book and student CRUD, duplicate validation, unavailable-book prevention, issue and return operations, duplicate-return prevention, and deletion of books with issue history.

## Future Scope

- Add librarian authentication and roles.
- Add fines and due dates.
- Add pagination and reporting.
- Add email notifications.
- Export records to PDF or CSV.

## Conclusion

The Library Management System demonstrates Flask routing, Jinja templates, SQLite database operations, CRUD workflows, validation, responsive UI design, and transactional data handling.
