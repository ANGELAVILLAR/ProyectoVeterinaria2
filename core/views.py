from django.shortcuts import redirect, render, HttpResponse

from core.forms import ProductoForm
from .models import Contact, Producto

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def petshop(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'core/petshop.html', context)

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    contacts=Contact.objects.all()
    context= {'contacts':contacts}
    return render(request, 'core/contact.html', context)

def agregar(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    
    context = {'form': form}
    return render(request, 'producto/agregar.html', context)
    
