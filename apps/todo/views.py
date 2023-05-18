from django.shortcuts import render, redirect, get_object_or_404
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


def edit(request, id):
    return render(request, 'todo/index.html', {
        'title': 'Todo',
        'todos': Todo.objects.all(),
        'todo': get_object_or_404(Todo, id=id),
    })


def update(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.name = request.POST.get('name')
    todo.save()
    return redirect('todo-index')


def finish(request, id, status):
    todo = get_object_or_404(Todo, id=id)
    if status == "False":
        todo.status = True
    else:
        todo.status = False

    todo.save()
    return redirect('todo-index')


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo-index')
