# core/context_processors.py
from core.utils import get_installed_apps_with_subapps

def installed_apps(request):
    """
    Контекстный процессор для получения списка установленных приложений и их подприложений.
    """
    return {
        'installed_apps': get_installed_apps_with_subapps(),
    }
