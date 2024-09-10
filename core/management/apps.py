# core/management/apps.py

from django.apps import AppConfig

class ManagementConfig(AppConfig):
    name = 'core.management'
    verbose_name = 'Управление платформой'
    description = """
    Подприложение Management отвечает за внутренние инструменты управления платформой, 
    такие как создание файлов, администрирование и прочие системные операции, необходимые для поддержки платформы.
    """
