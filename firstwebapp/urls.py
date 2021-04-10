from django.urls import path

from firstwebapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("another", views.another, name="Another"),
    path("anotherfunction", views.anotherfunction, name="AnotherFunction")
]
