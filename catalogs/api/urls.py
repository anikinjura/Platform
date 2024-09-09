# catalogs/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Регистрируем API роуты здесь, как только появятся новые viewsets

urlpatterns = [
    path('', include(router.urls)),
]
