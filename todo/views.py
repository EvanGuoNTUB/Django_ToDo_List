from django.shortcuts import render,get_object_or_404,redirect

from .models import Todo
from .forms import TodoModelForm


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def show(request,pk):
    #post = Post.objects.get(pk=pk)
    todos =  get_object_or_404(Todo,pk=pk)
    return render(request,'todo/show.html',{
        'todos': todos
    })


def new(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:index')

    return render(request, 'todo/new.html', {'form': form})

def edit(request,pk):
    todos = get_object_or_404(Todo, pk=pk)
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:index')
    return render(request, 'todo/edit.html', {
        'form': form
    })

def delete(request,pk): #非正統
    todos = get_object_or_404(Todo, pk=pk)
    todos.delete()
    return redirect('todo:index')