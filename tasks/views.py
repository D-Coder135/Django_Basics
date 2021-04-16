from django.shortcuts import render

tasks = ["Wake Up!", "Code", "Eat", "Sleep!"]


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks/add.html")
