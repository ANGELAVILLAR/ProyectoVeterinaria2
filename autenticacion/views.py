
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm
# Create your views here.

#******** CONTROL DE INGRESO DE USUARIOS  ***********************************************************
def login(request):
    if request.method != 'POST':
        return render(request, 'login/logear.html')
    email = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(email=email, password=password)

    if user is None:
        return render(request, 'login/logear.html', {'alarma': 'Correo o password no valido!'})
    auth.login(request, user)
    return render(request, 'core/home.html')


#********* DESACTIVACION DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')



def registrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            username = email.split('@')[0]

            existe = Usuario.objects.filter(email=email).exists()
            if not existe:
                user = Usuario.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.is_active = True
                user.save()
                return render(request, 'login/logear.html')
        else:
            return render(request, 'autenticacion/registro.html', {'form': form})

    else:
        form = UsuarioForm()
        return render(request, 'autenticacion/registro.html', {'form': form})
