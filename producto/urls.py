from django.contrib import admin
from django.urls import path, include
from producto import views


urlpatterns = [
    path("", views.petshop, name="petshop"),
]
