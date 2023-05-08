from django.contrib import admin
from .models import Articulo,Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo,ArticuloAdmin)
