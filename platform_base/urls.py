# platform_base/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('', include('core.urls')),   # Подключаем маршруты из приложения core
]
