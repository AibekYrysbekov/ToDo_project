from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'config/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
def create(request):
    title = request.POST['title']
    description = request.POST['description']
    todo = ToDo(title=title, description=description)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()

    context = {
        'title': todo.title,
        'description': todo.description,
    }
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


def edit_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo.title = title
        todo.description = description
        todo.save()
        return redirect('index')

    context = {
        'todo': todo,
    }
    return render(request, 'edit_todo.html', context)
