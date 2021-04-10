# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, this is my first web app.")


def another(request):
    return HttpResponse("Hello, User!")


def anotherfunction(request):
    return HttpResponse("This is just another view of my page!")
