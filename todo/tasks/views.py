from django.shortcuts import render, redirect
from .models import Task


def task_list(request):

    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect("/")

    tasks = Task.objects.all()

    return render(request, "tasks/list.html", {"tasks": tasks})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/")


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect("/")