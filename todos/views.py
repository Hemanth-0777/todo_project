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