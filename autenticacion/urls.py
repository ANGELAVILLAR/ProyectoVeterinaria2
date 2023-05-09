from django.contrib import admin
from django.urls import path
from .views import Registro,View
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', Registro.as_view(), name="autenticacion"),
    # path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]