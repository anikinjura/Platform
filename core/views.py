# core/views.py

from django.views.generic import TemplateView

APPS = [
    {
        'name': 'Catalogs',
        'display_name': 'Справочники',
        'url_name': 'core:application_detail',
        'description': 'Управление справочниками системы.',
        'subapps': [
            {'name': 'Agents', 'display_name': 'Агенты', 'url': '/catalogs/agents/'},
            {'name': 'Pickup Points', 'display_name': 'Пункты выдачи', 'url': '/catalogs/pickup-points/'}
        ]
    },
    {
        'name': 'Documents',
        'display_name': 'Документы',
        'url_name': 'core:application_detail',
        'description': 'Фиксация событий в системе.',
        'subapps': [
            {'name': 'Orders', 'display_name': 'Заказы', 'url': '/documents/orders/'},
            {'name': 'Deliveries', 'display_name': 'Доставки', 'url': '/documents/deliveries/'}
        ]
    },
    {
        'name': 'Registers',
        'display_name': 'Реестры',
        'url_name': 'core:application_detail',
        'description': 'Записи о событиях и накопленные итоги.',
        'subapps': []
    },
    {
        'name': 'Reports',
        'display_name': 'Отчёты',
        'url_name': 'core:application_detail',
        'description': 'Извлечение и визуализация данных.',
        'subapps': []
    }
]

# Базовые утилиты ядра
MANAGEMENT_TOOLS = [
    {'name': 'Выгрузка текста из файлов каталога', 'url': '/management/file-export/'},
    # Другие утилиты ядра
]

class IndexView(TemplateView):
    template_name = 'core/index.html'

class ApplicationDetailView(TemplateView):
    # Временная "заглушка" для тестирования работы. Далее будем идти в конкретный объект метаданных (сейчас не создан)
    template_name = 'core/application_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем имя текущего приложения, полученное из URL
        context['app_name'] = kwargs.get('app_name')
        return context