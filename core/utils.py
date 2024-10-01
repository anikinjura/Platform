from django.conf import settings
from django.apps import apps
import os

EXCLUDED_APPS = ['rest_framework', 'drf_yasg', 'django_extensions']

def get_installed_apps_with_subapps():
    """
    Возвращает список базовых приложений и их подприложений.
    Собирает информацию о verbose_name и description, если они заданы.
    """
    installed_apps = settings.INSTALLED_APPS

    # Фильтрация системных приложений
    platform_apps = [app for app in installed_apps if not app.startswith('django.') and app not in EXCLUDED_APPS]

    app_structure = {}
    for app in platform_apps:
        if '.' in app:  # Пропускаем подприложения, зарегистрированные через точку
            continue

        try:
            app_config = apps.get_app_config(app.split('.')[-1])
            app_structure[app_config.label] = {
                'name': app_config.name,
                'verbose_name': getattr(app_config, 'verbose_name', app_config.name),
                'description': getattr(app_config, 'description', 'Нет описания'),
                'path': app_config.path,
                'sub_apps': get_sub_apps(app_config.path, app_config.name)
            }
        except LookupError:
            continue

    return app_structure

def get_sub_apps(base_app_path, base_app_name):
    """
    Возвращает список подприложений, находящихся в директории базового приложения.
    Подприложения идентифицируются по наличию файла apps.py.
    """
    sub_apps = []
    try:
        for entry in os.scandir(base_app_path):
            if entry.is_dir() and os.path.exists(os.path.join(entry.path, 'apps.py')):
                sub_apps.append(entry.name)
    except FileNotFoundError:
        pass

    return sub_apps
