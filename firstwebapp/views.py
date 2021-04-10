# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hey, this is my first web app.")
    return render(request, "firstwebapp/index.html")  # To show a full html file as a response when the address in
    # searched

def another(request):
    return HttpResponse("Hello, User!")


def anotherfunction(request):
    return HttpResponse("This is just another view of my page!")


def greet(response, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
