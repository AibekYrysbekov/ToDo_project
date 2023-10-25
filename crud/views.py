from django.shortcuts import render
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'config/index.html', {'todo_list': todos, 'title': 'Главная страница'})