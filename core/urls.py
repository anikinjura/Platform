# core/urls.py

from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views

app_name = 'core'

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Platform API",
        default_version='v1',
        description="API документация для платформы",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@platform.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Маршруты для отображения структуры приложений и подприложений
    path('', views.IndexView.as_view(), name='index'),
    path('application/<str:app_name>/', views.ApplicationDetailView.as_view(), name='application_detail'),
    path('application/<str:app_name>/<str:subapp_name>/', views.SubApplicationDetailView.as_view(), name='subapplication_detail'),

    # Подключение маршрутов API
    path('api/', include('core.api.urls')),

    # Маршруты для документации Swagger и Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
