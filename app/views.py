from django.shortcuts import render
from .models import *
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
    
def  update(request, pk):
    TO = Todo.objects.get(pk=pk)
    d = {'TO': TO}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO.title = title
        TO.desc = desc
        TO.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'update.html', d)

def delete(request, pk):
    TO = Todo.objects.get(pk=pk)
    TO.delete()
    return HttpResponseRedirect(reverse('home'))