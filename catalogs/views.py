# catalogs/views.py

from django.views.generic import ListView, DetailView
from .models import CatalogBase

class IndexView(ListView):
    model = CatalogBase
    template_name = 'catalogs/index.html'
    context_object_name = 'catalog_list'

class CatalogDetailView(DetailView):
    model = CatalogBase
    template_name = 'catalogs/catalog_detail.html'
    context_object_name = 'catalog'
