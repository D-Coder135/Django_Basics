from django.urls import path

from firstwebapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("another", views.another, name="Another"),
    path("anotherfucntion", views.anotherfunction, name="AnotherFunction")
]
