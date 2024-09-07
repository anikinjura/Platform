# core/api/serializers.py
from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор, который можно наследовать для стандартных моделей.
    """
    class Meta:
        model = None  # Этот атрибут должен быть установлен в наследуемом классе
        fields = '__all__'  # По умолчанию возвращаем все поля модели
