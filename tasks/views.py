from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    #     return an empty list of task if there isn't any tasks present already for a particular session.
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
        # Rendering request.session["tasks"] instead of rendering the global variable tasks(which is commented out).
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)  # Here by writing request.POST inside the () means that we are taking all of
        # data inserted by the user and filling it to the NewTaskForm i.e a new form which is created.
        if form.is_valid():
            task = form.cleaned_data["task"]  # Here we are storing all the task entered by the user inside the task
            # field.
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        # Here we are redirecting the page back to tasks page by calling django reverse method which will automatically
        # figure out the url of the index of the tasks app is and use that url to where we want to redirect by using
        # HttpResponseRedirect() method.
        # Here, the HttpResponseRedirect() and the reverse() method are already built in Django.
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    #     Returning the add.html page again but instead of providing a new form, here we are providing the existing form
    #     data. So that we can display information about any errors that come as well.
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
# Give this access to a variable called field which is a NewTaskForm() that means providing an empty form.
