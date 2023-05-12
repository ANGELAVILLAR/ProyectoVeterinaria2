from django.db import models
from django.contrib.auth import get_user_model
from articulo.models import Articulo
from django.db.models import F,Sum, FloatField

# Create your models here.
User=get_user_model()
class Pedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=sum(f("precio")*f("cantidad"),autput_field=FloatField())            
        )["total"]
    
    
    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']
        
class LineaPedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.articulo_id.name}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name='lineapedido'
        verbose_name_plural='Lineas Pedidos'
        ordering=['id']
    
    