To-do list project
Create a project folder
Let's create a folder called:
Create the virtual environment
Now run:
py -3.12 -m venv todoenv
❌ PowerShell blocked the Activate.ps1 script.
Best solution for your Django project
Since you're using PowerShell, run this command:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
todoenv\Scripts\activate
Check Python inside the virtual environment
Run:
python --version
Upgrade pip
Now:
python -m pip install --upgrade pip
Install Django
Now install Django:
python -m pip install django
Django's official Windows instructions use pip inside an activated virtual environment. 
Check Django:
django-admin --version
Create the Django project
Now run:
django-admin startproject todo_project
DjangoProjects
│
├── todoenv
│
└── todo_project
    │
    ├── manage.py
    │
    └── todo_project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
Enter the project
cd todo_project
Run the Django server
Run:
python manage.py runserver
You should see something similar to:
Starting development server at http://127.0.0.1:8000/
Understand manage.py
This file is extremely important.
manage.py
is used for Django project commands.
For example:
python manage.py runserver
python manage.py startapp todos
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Think of:
manage.py
as the control center for your Django project.
Create the Todo application
A Django project can contain multiple apps.
Our project:
todo_project
will contain an application:
todos
Run:
python manage.py startapp todos
todo_project
│
├── manage.py
│
├── todo_project
│
└── todos
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── tests.py
    └── views.py
Register the Todo app
Open:
todo_project/settings.py
Find:
INSTALLED_APPS = [
Add:
'todos',
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'todos',
]
Create the Todo model
Open:
todos/models.py
Replace its contents with:
from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
Field	Purpose
title	Todo description
completed	Completed or not
created_at	Date/time created
Create the database migration
Run:
python manage.py makemigrations
You should get something like:
Migrations for 'todos':
  todos\migrations\0001_initial.py
Now:
python manage.py migrate
Django will create the database tables.
You'll notice a new file:
db.sqlite3
SQLite is Django's default database for a basic project.
Register Todo in Django Admin
Open:
todos/admin.py
Add:
from django.contrib import admin
from .models import Todo
admin.site.register(Todo)
Now Django Admin can manage our Todo objects.
Create the Todo view
Open:
todos/views.py
from django.shortcuts import render, redirect
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Todo.objects.create(title=title)

        return redirect('todo_list')

    return render(request, 'todos/todo_list.html', {'todos': todos})


def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()

    return redirect('todo_list')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect('todo_list')
Create URLs for the Todo app
Inside the todos folder create:
urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
Connect app URLs to project URLs
Open:
todo_project/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
]
Create the templates folder
Inside the todos application create:
templates
Inside that:
todos
Inside that:
todo_list.html
todos
│
├── templates
│   └── todos
│       └── todo_list.html
│
├── models.py
├── views.py
├── urls.py
└── admin.py
Create the HTML page
Open:
todo_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 40px;
        }

        .container {
            width: 600px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
        }

        form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input {
            flex: 1;
            padding: 10px;
        }

        button {
            padding: 10px 15px;
            cursor: pointer;
        }

        ul {
            padding: 0;
        }

        li {
            list-style: none;
            padding: 12px;
            margin-bottom: 10px;
            background: #eee;
            display: flex;
            justify-content: space-between;
        }

        .completed {
            text-decoration: line-through;
            color: gray;
        }

        a {
            margin-left: 10px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>My Todo List</h1>

    <form method="POST">

        {% csrf_token %}

        <input
            type="text"
            name="title"
            placeholder="Enter a todo..."
            required
        >

        <button type="submit">
            Add Todo
        </button>

    </form>

    <ul>

        {% for todo in todos %}

            <li>

                <span class="{% if todo.completed %}completed{% endif %}">
                    {{ todo.title }}
                </span>

                <span>

                    <a href="{% url 'complete_todo' todo.id %}">
                        {% if todo.completed %}
                            Undo
                        {% else %}
                            Complete
                        {% endif %}
                    </a>

                    <a href="{% url 'delete_todo' todo.id %}">
                        Delete
                    </a>

                </span>

            </li>

        {% empty %}

            <li>No todos yet.</li>

        {% endfor %}

    </ul>

</div>

</body>
</html>

(todoenv) PS C:\my_projects\todo_project> python manage.py check
System check identified no issues (0 silenced).
Create the migration
Run:
python manage.py makemigrations
Apply the migration
Now run:
python manage.py migrate
You should see several migrations being applied, including something similar to:
Applying todos.0001_initial... OK

Run the application
Run:
python manage.py runserver
control flow
                 USER
                   ↓
              Browser
                   ↓
              HTTP Request
                   ↓
          project/urls.py
                   ↓
           todos/urls.py
                   ↓
              views.py
                   ↓
              models.py
                   ↓
              Database
                   ↓
             Todo Objects
                   ↓
              views.py
                   ↓
              Template
                   ↓
                HTML
                   ↓
              Browser

What happens when you ADD a Todo
Browser
   ↓
POST request
   ↓
URL
   ↓
View
   ↓
Model
   ↓
Database
   ↓
Redirect
   ↓
View
   ↓
Template
   ↓
Browser

What happens when you DELETE?
Click Delete
     ↓
Browser sends request
     ↓
URL
     ↓
delete_todo()
     ↓
Todo.objects.get(id)
     ↓
Database
     ↓
todo.delete()
     ↓
Database record deleted
     ↓
redirect()
     ↓
todo_list()
     ↓
Database
     ↓
Template
     ↓
Browser

Let’s push the project in GitHub
Download and install git from below website
https://git-scm.com/install/windows
After installation:
1.	Close CMD 
2.	Open a new CMD 
3.	Run: 
git --version
You need to navigate inside todo_project (the outer folder containing manage.py).
Run this command in your terminal:
cd todo_project
create a repository in github
you will get a link of your repo
https://github.com/viveksirji/projects.git
Run these 3 commands in your VS Code terminal (make sure your prompt shows PS C:\my_projects\todo_project>):
git branch -M main
git remote add origin https://github.com/viveksirji/projects.git
getting error now you have to create the email and username
git config --global user.email vivekpandeygtechtrainer@gmail.com
git config --global user.name "Vivek Pandey"
git init
Initialized empty Git repository in C:/my_projects/todo_project/.git/
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
it will ask you to authorize with the github access 




