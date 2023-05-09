from django.db import models

class Categoria(models.Model):    
    name=models.CharField(max_length=100)     
    created=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.name

class Articulo(models.Model):
    reference=models.IntegerField(max_length=30)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6, decimal_places=1)
    category=models.ManyToManyField(Categoria)    
    imagen=models.ImageField(upload_to='articulo')    
    created=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='articulo'
        verbose_name_plural='articulos'
        
    def __str__(self):
        return self.name


# Create your models here.
