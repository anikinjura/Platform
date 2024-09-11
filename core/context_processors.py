# core/context_processors.py

from .views import APPS

def apps_context(request):
    return {'APPS': APPS}
