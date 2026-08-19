# Django To-Do List Application

A responsive web-based To-Do List application built with Django, SQLite, and CSS. Features include task creation, status toggling (complete/undo), and item deletion.

---

## Features

* **Task Management**: Add, complete, toggle, and delete tasks in real time.
* **Admin Integration**: Built-in Django Admin setup to manage task records easily.
* **Persistent Storage**: Task ordering and storage managed via SQLite database.

---

## Tech Stack

* **Backend**: Python 3.12, Django
* **Database**: SQLite
* **Frontend**: HTML5, Modern CSS

---

## Quick Start Guide

### 1. Setup Virtual Environment
```powershell
# Create virtual environment
py -3.12 -m venv todoenv

# Set execution policy (if blocked on Windows)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate virtual environment
todoenv\Scripts\activate

2. Install Dependencies

python -m pip install --upgrade pip
python -m pip install django

3. Database Migration & Setup
python manage.py makemigrations
python manage.py migrate

4. Run Development Server

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to run the application.

Application Architecture Flow
User Request ──> URL Router ──> View (Controller) ──> Model (Database)
                                      │
User Browser <── HTML Template <──────┘


File Structure

todo_project/
│
├── manage.py
├── db.sqlite3
├── todo_project/          # Project configurations
│   ├── settings.py
│   └── urls.py
└── todos/                 # Application module
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/todos/
        └── todo_list.html
