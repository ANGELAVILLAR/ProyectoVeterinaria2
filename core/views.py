from django.shortcuts import render, HttpResponse
from .models import Contact

def home(request):
    contacts=Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'core/home.html', context)

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")


