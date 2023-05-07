from django.db import models

#created your models here.
class Category(models.Model):
    name_cat = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name_cat']

        def __str__(self):
            return self.name_cat
class Producto(models.Model):
    reference=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    image=models.ImageField(verbose_name="Imagen", upload_to="productos", null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    categories=models.ManyToManyField(Category, verbose_name="Categorias")   
    class Meta:
            verbose_name = "Producto"
            verbose_name_plural = "Productos"
            ordering = ['name']

            def __str__(self):
                return self.name
        