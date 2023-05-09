from django.contrib import admin
from .models import Contact
from core.models import Contact

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display=("name","email","phone")
    search_fields=("name","phone")
