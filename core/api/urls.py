# core/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TestViewSet

router = DefaultRouter()
router.register(r'test', TestViewSet, basename='test') # тестовая регистрация роутера для API
# Здесь будут зарегистрированы все viewsets от объектов метаданных

urlpatterns = [
    path('', include(router.urls)),
]
