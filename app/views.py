from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home(request):
    all_todos=Todo.objects.all()
    d={'all_todos':all_todos}
    if request.method == "POST":
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        TO=Todo(title=title , desc=desc)
        TO.save()
    return render(request, 'home.html' ,d)



def update_todo(request, todo_id):
    todo = Todo.get.object(Todo, id=todo_id)
    
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.desc = request.POST.get('desc')
        todo.save()
        return redirect('home')  
    
    return render(request, 'update_todo.html', {'todo': todo})


def delete_todo(request, todo_id):
    todo =Todo.get.object(Todo, id=todo_id)
    
    if request.method == "POST":
        todo.delete()
        return redirect('home')  
    
    return render(request, 'delete_todo.html', {'todo': todo})
