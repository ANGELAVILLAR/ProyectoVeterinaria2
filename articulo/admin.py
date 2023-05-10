from django.contrib import admin
from .models import Articulo,Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display = ('name', 'created','updated')    

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display = ('reference','name', 'price','created','updated')
    search_fields=('reference','name')


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo,ArticuloAdmin)
