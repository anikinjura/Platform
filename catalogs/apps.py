# catalogs/apps.py

from django.apps import AppConfig

class CatalogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogs'
    verbose_name = 'Справочники'
    description = "Является базовым приложением для всех справочников системы."
