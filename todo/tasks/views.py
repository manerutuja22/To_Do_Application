from django.shortcuts import render,redirect
from .models import task
# Create your views here.
def task_list(request):

    if request.method == "POST":
        title = request.POST.get("title")
        task.objects.create(title=title)
        return redirect("/")

    tasks = task.objects.all()

    return render(request, "tasks/list.html", {"tasks": tasks})