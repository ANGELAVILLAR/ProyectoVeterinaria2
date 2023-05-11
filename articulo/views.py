from unicodedata import category
from django.shortcuts import render
from articulo.models import Articulo,Categoria
from django.contrib.auth.decorators import login_required
from carro.carro import Carro


# Create your views here.
# @login_required(redirect_field_name="logear.html")
def petshop(request):
    articulo=Articulo.objects.all()
    return render(request, "articulos/petshop.html",{"articulo":articulo})

# def categoria(request,categoria_id):
#     categoria=Categoria.objects.get(id=categoria_id )
#     articulo=Articulo.objects.filter(category=categoria)    
#     return render(request, "articulos/categoria.html",{'categoria':categoria},{'articulo':articulo})