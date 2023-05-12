from django.urls import path
from . import views

app_name="pedido"

urlpatterns = [
    
    path('pedido/', views.procesar_pedido, name="procesar_pedido"),
    # path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]