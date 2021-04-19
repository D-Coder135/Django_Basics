from django import forms
from django.shortcuts import render

tasks = ["Wake Up!", "Code", "Eat", "Sleep!"]


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)  # Here by writing request.POST inside the () means that we are taking all of
        # data inserted by the user and filling it to the NewTaskForm i.e a new form which is created.
        if form.is_valid():
            task = form.cleaned_data["task"]
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
# Give this access to a variable called field which is a NewTaskForm()
