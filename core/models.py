from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    messageContact=models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
        
# Create your models here.
