from django.shortcuts import render,redirect

from articulo.admin import ArticuloAdmin
from .carro import Carro
from articulo.models import Articulo

# Create your views here.
def agregar_articulo(request, articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=ArticuloAdmin)
    carro.agregar(articulo=articulo)
    return redirect("articulo")

def eliminar_articulo(request, articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=ArticuloAdmin)
    carro.eliminar(articulo=articulo)
    return redirect("articulo")

def restar_articulo(request, articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=ArticuloAdmin)
    carro.restar_articulo(articulo=articulo)
    return redirect("articulo")

def limpiar_carro(request, articulo_id):
    carro=Carro(request)    
    carro.limpiar_carro()
    return redirect("articulo")