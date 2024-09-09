from rest_framework import serializers
from core.api.serializers import BaseSerializer

class CatalogBaseSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = None  # Будет устанавливаться в наследуемых классах
        fields = '__all__'
