from django.shortcuts import render,get_object_or_404,redirect

from .models import Todo
from .forms import TodoModelForm,DeleteConfirmForm
from django.contrib.auth.decorators import login_required


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def show(request,pk):
    #post = Post.objects.get(pk=pk)
    todo =  get_object_or_404(Todo,pk=pk)
    return render(request,'todo/show.html',{
        'todo': todo
    })

@login_required
def new(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.creator = request.user
        todo.save()
        return redirect('todo:index')

    return render(request, 'todo/new.html', {'form': form})

@login_required
def edit(request,pk):
    todos = get_object_or_404(Todo, pk=pk)
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.creator = request.user
        todo.save()
        return redirect('todo:index')
    return render(request, 'todo/edit.html', {
        'form': form
    })

@login_required
def delete(request,pk): #非正統

    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        todos = get_object_or_404(Todo, pk=pk)
        todos.delete()
        return redirect('todo:index')


    return render(request,'todo/delete.html',{'form':form})