from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    return render(request, 'todo/index.html', {
        'title': 'Todo',
        'todos': Todo.objects.all(),
    })


def store(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        Todo.objects.create(
            name=form.cleaned_data['name'],
            status=0,
        )
    return redirect('todo-index')
