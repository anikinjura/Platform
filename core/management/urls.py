# core/management/urls.py

from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('file-export/', views.file_export_view, name='file_export'),
]
