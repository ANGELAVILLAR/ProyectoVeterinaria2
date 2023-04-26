from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    messageContact=models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
        

class Producto(models.Model):
    reference=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    category=models.CharField(max_length=50)   
    def __str__(self):
        return self.name
        
