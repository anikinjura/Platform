# core/management/views.py

from django.shortcuts import render
from django.http import HttpResponse
import os

def file_export_view(request):
    '''
    Представление для веб-интерфейса выгрузки файлов. 
    Позволяет выбрать директорию для выгрузки файлов и указать параметры.
    '''
    if request.method == 'POST':
        directory = request.POST.get('directory')  # Получаем путь к директории
        if os.path.exists(directory):
            # Здесь мы можем добавить логику для обработки файлов в директории
            result = f'Файлы из директории {directory} успешно выгружены.'
            return HttpResponse(result)
        else:
            return HttpResponse('Указанная директория не существует.')

    return render(request, 'management/file_export.html')
