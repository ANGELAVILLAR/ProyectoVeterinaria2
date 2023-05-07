from django.contrib import admin
from .models import Contact
from core.models import Contact

class ContactoAdmin(admin.ModelAdmin):
    list_display=("name","email","phone")
    search_fields=("name","phone")

admin.site.register(Contact,ContactoAdmin)