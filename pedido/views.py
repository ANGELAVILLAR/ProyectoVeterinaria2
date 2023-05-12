from multiprocessing import Value
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from .models import LineaPedido, Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            articulo_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.name,
        emailusuario=request.user.mail
    )
    
    messages.secces(request, "El pediso se a realizado de forma correcta")
    
    return redirect("../articulo")

def enviar_mail(**kwargs):
    asunto="Informacion de pedido"
    mensaje=render_to_string("email/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreususario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="cristianascencio34@gmail.com"
    to=kwargs.get("emailusuario")
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)
    
