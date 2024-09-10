# catalogs/admin.py

from django.contrib import admin
from .models import CatalogBase

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

# admin.site.register(CatalogBase, CatalogAdmin)
