from django.shortcuts import render
from .models import Producto

# Create your views here.

def petshop(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    return render(request, 'petshop.html', context)