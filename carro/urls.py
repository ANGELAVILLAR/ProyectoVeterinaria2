from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="carro"

urlpatterns = [
    
    path('agregar/<int:articulo_id>/', views.agregar_articulo, name="agregar"),
    path('eliminar/<int:articulo_id>/', views.eliminar_articulo, name="eliminar"),
    path('restar/<int:articulo_id>/', views.restar_articulo, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
    # path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]