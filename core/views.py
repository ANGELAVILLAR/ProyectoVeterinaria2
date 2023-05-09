from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from .models import Contact


def home(request):
    carro=Carro(request)
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    contacts=Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'core/contact.html', context)

# def login(request):
#     return render(request, "core/login.html")


