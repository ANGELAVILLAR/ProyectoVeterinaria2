from django.db import models

class Producto(models.Model):
    reference=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    category=models.CharField(max_length=50)   
    def __str__(self):
        return self.name
        