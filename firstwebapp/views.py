# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, this is my first web app.")
