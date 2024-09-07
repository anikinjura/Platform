# core/api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class TestViewSet(viewsets.ViewSet):
    """
    Чтобы маршрут /api/ начал работать, нужно зарегистрировать хотя бы один ViewSet в роутере.
    Это тестовый ViewSet
    """
    def list(self, request):
        return Response({"message": "API is working!"})

class BaseViewSet(viewsets.ViewSet):
    """
    Базовый ViewSet, который можно наследовать для создания стандартных API.
    """

    queryset = None  # Этот атрибут должен быть установлен в наследуемом классе
    serializer_class = None  # Этот атрибут должен быть установлен в наследуемом классе

    def list(self, request):
        """
        Получить список объектов.
        """
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Получить конкретный объект по ID.
        """
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        except self.queryset.model.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        Создать новый объект.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Обновить существующий объект.
        """
        try:
            instance = self.queryset.get(pk=pk)
        except self.queryset.model.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Удалить объект.
        """
        try:
            instance = self.queryset.get(pk=pk)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except self.queryset.model.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
