from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path("", views.home,name="home"),
    #path('usuario/', include('appUsuarios.urls')),
]
