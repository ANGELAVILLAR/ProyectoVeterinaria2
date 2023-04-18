from django.db import models
class Tarea(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    
        
# Create your models here.
