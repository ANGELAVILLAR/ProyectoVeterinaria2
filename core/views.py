from django.shortcuts import render, HttpResponse
from .models import Contact, Producto

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def petshop(request):
    return render(request, "producto/petshop.html")


def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    contacts=Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'core/contact.html', context)

def petshop(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'core/petshop.html', context)

