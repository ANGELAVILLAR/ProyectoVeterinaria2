#from django.shortcuts import redirect, render

# Create your views here.
#from producto.forms import ProductoForm
#from .models import Producto

#def petshop(request):
    #productos=Producto.objects.all()
    #context={'productos':productos}
    #return render(request, 'core/petshop.html', context)

#def agregar(request):
    #if request.method == "POST":
        #form = ProductoForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('home')
    #else:
        #form = ProductoForm()
    
    #context = {'form': form}
    #return render(request, 'producto/agregar.html', context)