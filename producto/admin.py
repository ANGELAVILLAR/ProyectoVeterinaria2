from django.contrib import admin
from .models import Category, Producto

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, categoryAdmin)
admin.site.register(Producto, ProductoAdmin)