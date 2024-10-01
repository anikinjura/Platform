from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Ядро платформы"
    description = "Основное приложение платформы. Содержит базовый функционал платформы."
