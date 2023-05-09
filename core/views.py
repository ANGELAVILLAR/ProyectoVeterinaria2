from django.shortcuts import render
from .models import Contact
from servicios.models import Servicio


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    servicios=Servicio.objects.all()
    return render(request, "core/portfolio.html", {'servicios': servicios})

def contact(request):
    contacts=Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'core/contact.html', context)

def login(request):
    return render(request, "core/login.html")

