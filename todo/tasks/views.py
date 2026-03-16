from django.shortcuts import render
from .models import task
# Create your views here.
def task_list(request):
  tasks = task.objects.all()
  return render (request,'tasks/index.html',{tasks: tasks})