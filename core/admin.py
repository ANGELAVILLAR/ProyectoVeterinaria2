from django.contrib import admin
from .models import Contact
from .models import Producto

admin.site.register(Producto)
admin.site.register(Contact)