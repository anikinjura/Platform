from rest_framework import viewsets
from core.api.views import BaseViewSet

class CatalogBaseViewSet(BaseViewSet):
    queryset = None  # Будет устанавливаться в наследуемых классах
    serializer_class = None  # Будет устанавливаться в наследуемых классах
