from django.urls import path

from firstwebapp import views

urlpatterns = [
    path("", views.index, name="index")
]
