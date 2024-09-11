# core/context_processors.py

from .views import APPS, MANAGEMENT_TOOLS

def apps_context(request):
    """
    Добавляет список объектов метаданных (приложений) и утилит управления в контекст всех шаблонов.
    """
    return {
        'apps': APPS,
        'management_tools': MANAGEMENT_TOOLS,
    }
