from django.conf import settings
from django.apps import apps


def get_installed_apps_with_subapps():
    """
    Возвращает список базовых приложений и их подприложений.
    Собирает информацию о verbose_name и description, если они заданы.
    """
    custom_apps = settings.CUSTOM_APPS

    app_structure = {}
    for app in custom_apps:
        # Пропускаем подприложения, зарегистрированные через точку
        if '.' in app:
            continue

        try:
            # Получаем конфигурацию базового приложения
            app_config = apps.get_app_config(app.split('.')[-1])
            app_structure[app_config.label] = {
                'name': app_config.name,
                'verbose_name': getattr(app_config, 'verbose_name', app_config.name),
                'description': getattr(app_config, 'description', 'Описание отсутствует'),
                'path': app_config.path,
                'sub_apps': get_sub_apps(app, custom_apps)  # Получаем подприложения
            }
        except LookupError:
            continue

    return app_structure


def get_sub_apps(base_app_name, custom_apps):
    """
    Возвращает список подприложений, зарегистрированных в Django как дочерние.
    Используем метод apps.get_app_config для извлечения verbose_name подприложений.
    """
    sub_apps = []

    # Ищем все приложения, зарегистрированные через точку после имени базового приложения
    for app in custom_apps:
        if app.startswith(base_app_name + '.'):
            try:
                sub_app_config = apps.get_app_config(app.split('.')[-1])
                sub_apps.append({
                    'name': sub_app_config.name,
                    'verbose_name': getattr(sub_app_config, 'verbose_name', sub_app_config.name),
                    'description': getattr(sub_app_config, 'description', 'Описание отсутствует')
                })
            except LookupError:
                continue

    return sub_apps
