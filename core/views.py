# core/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Базовые приложения (объекты метаданных) и их подприложения
APPS = [
    {
        'name': 'Catalogs',
        'url_name': 'core:application_detail',
        'description': 'Управление справочниками системы.',
        'subapps': [
            {'name': 'Agents', 'url': '/catalogs/agents/'},
            {'name': 'Pickup Points', 'url': '/catalogs/pickup-points/'}
        ]
    },
    {
        'name': 'Documents',
        'url_name': 'core:application_detail',
        'description': 'Фиксация событий в системе.',
        'subapps': [
            {'name': 'Orders', 'url': '/documents/orders/'},
            {'name': 'Deliveries', 'url': '/documents/deliveries/'}
        ]
    },
    {
        'name': 'Registers',
        'url_name': 'core:application_detail',
        'description': 'Записи о событиях и накопленные итоги.',
        'subapps': []
    },
    {
        'name': 'Reports',
        'url_name': 'core:application_detail',
        'description': 'Извлечение и визуализация данных.',
        'subapps': []
    }
]

# Базовые утилиты ядра
MANAGEMENT_TOOLS = [
    {'name': 'Выгрузка файлов', 'url': '/management/file-export/'},
    # Другие утилиты ядра
]

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apps'] = APPS
        context['management_tools'] = MANAGEMENT_TOOLS  # Передаем утилиты в контекст
        return context

class ApplicationDetailView(TemplateView):
    template_name = 'core/application_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_name = kwargs.get('app_name')
        context['application'] = next(app for app in APPS if app['name'] == app_name)
        context['subapps'] = [
            {'name': 'Entities', 'url_name': 'core:subapplication_detail', 'description': 'Управление сущностями в выбранном приложении.'},
        ]
        return context

class SubApplicationDetailView(TemplateView):
    template_name = 'core/subapplication_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_name = kwargs.get('app_name')
        subapp_name = kwargs.get('subapp_name')
        context['subapplication'] = {
            'name': subapp_name,
            'description': f'Функционал подприложения {subapp_name}'
        }
        return context
