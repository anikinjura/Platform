# core/management/commands/generate_subapp.py

import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Генерация подприложений для базовых приложений платформы'

    def add_arguments(self, parser):
        parser.add_argument('--app_name', type=str, help='Имя базового приложения (например, Catalogs)')
        parser.add_argument('--subapp_name', type=str, help='Имя подприложения (например, Agent)')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        subapp_name = kwargs['subapp_name']
        
        # Указываем пути
        base_dir = os.path.join('apps', app_name.lower(), subapp_name.lower())
        os.makedirs(base_dir, exist_ok=True)
        
        # Создаем файлы подприложения (например, views.py, urls.py, templates)
        self.create_file(base_dir, 'views.py', self.generate_views_code(subapp_name))
        self.create_file(base_dir, 'urls.py', self.generate_urls_code(subapp_name))
        self.create_template_file(base_dir, subapp_name)

        self.stdout.write(self.style.SUCCESS(f'Подприложение {subapp_name} для {app_name} создано.'))

    def create_file(self, directory, filename, content):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            file.write(content)

    def create_template_file(self, directory, subapp_name):
        template_dir = os.path.join(directory, 'templates', subapp_name.lower())
        os.makedirs(template_dir, exist_ok=True)
        template_path = os.path.join(template_dir, f'{subapp_name.lower()}_detail.html')
        with open(template_path, 'w') as file:
            file.write(f'<!-- Шаблон для {subapp_name} -->')

    def generate_views_code(self, subapp_name):
        return f"""
from django.shortcuts import render
from django.views.generic import TemplateView

class {subapp_name}DetailView(TemplateView):
    template_name = '{subapp_name.lower()}/{subapp_name.lower()}_detail.html'
"""

    def generate_urls_code(self, subapp_name):
        return f"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.{subapp_name}DetailView.as_view(), name='{subapp_name.lower()}_detail'),
]
"""
