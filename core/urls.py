# core/urls.py

from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('application/<str:app_name>/', views.ApplicationDetailView.as_view(), name='application_detail'), # временная "заглушка" для тестирования работы APPS

    path('management/', include('core.management.urls')),  # убираем namespace
]
