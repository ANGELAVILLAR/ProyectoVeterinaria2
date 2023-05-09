from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
class Registro(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "autenticacion/registro.html",{"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "autenticacion/registro.html",{"form":form})