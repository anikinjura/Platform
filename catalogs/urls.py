# catalogs/urls.py

from django.urls import path, include
from . import views

app_name = 'catalogs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.CatalogDetailView.as_view(), name='catalog_detail'),
    path('api/', include('catalogs.api.urls')),
]
