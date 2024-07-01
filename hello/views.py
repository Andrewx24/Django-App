from django.shortcuts import render

# Create your views here.
from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
]