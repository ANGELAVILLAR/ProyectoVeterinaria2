from django.contrib import admin
from django.urls import path
from .views import Registro,  cerrar_sesion,logear
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', Registro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    # path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]