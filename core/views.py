# core/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Список базовых приложений (пока статичный, позже можем автоматизировать)
APPS = [
    {'name': 'Справочники', 'url_name': 'core:application_detail', 'description': 'Управление справочниками системы.'},
    {'name': 'Документы', 'url_name': 'core:application_detail', 'description': 'Фиксация событий в системе.'},
    {'name': 'Регистры', 'url_name': 'core:application_detail', 'description': 'Записи о событиях и накопленные итоги.'},
    {'name': 'Отчеты', 'url_name': 'core:application_detail', 'description': 'Извлечение и визуализация данных.'},
]

# Главная страница
class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apps'] = APPS
        return context

# Страница базового приложения
class ApplicationDetailView(TemplateView):
    template_name = 'core/application_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_name = kwargs.get('app_name')
        context['application'] = next(app for app in APPS if app['name'] == app_name)
        # Пока что статично, позже будет динамическое
        context['subapps'] = [
            {'name': 'Агенты', 'url_name': 'core:subapplication_detail', 'description': 'Управление агентами.'},
        ]
        return context

# Страница подприложения
class SubApplicationDetailView(TemplateView):
    template_name = 'core/subapplication_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_name = kwargs.get('app_name')
        subapp_name = kwargs.get('subapp_name')
        context['subapplication'] = {
            'name': subapp_name,
            'description': 'Функционал подприложения {}'.format(subapp_name)
        }
        return context
