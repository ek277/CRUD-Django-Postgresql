from pydoc import describe
from turtle import title
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    return render(request, 'list_tasks.html')

def create_task(request):
    task = Task(title = request.POST['title'], description = request.POST['description'])
    task.save()
    return redirect('/tasks/')