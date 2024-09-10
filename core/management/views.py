# core/management/views.py

from django.shortcuts import render
from django.http import HttpResponse
import os
from .utils import get_files_from_directory

def file_export_view(request):
    '''
    Представление для веб-интерфейса выгрузки кода файлов из указанной директории. 
    Позволяет выбрать директорию для выгрузки кода в файлах и указать параметры.
    '''
    file_contents = None  # Инициализация переменной для метода GET

    if request.method == 'POST':
        directory = request.POST.get('directory')  # Получаем путь к директории
        if os.path.exists(directory):
            # Используем утилиту для получения содержимого файлов
            file_contents = get_files_from_directory(directory)
            
            # Преобразуем содержимое файлов в строку для вывода
            result = "\n\n".join([f"### Код из файла: {path} ###\n\n{content}" for path, content in file_contents.items()])
            
            # Указываем правильную кодировку и тип контента
            return HttpResponse(result, content_type='text/plain; charset=utf-8')
        else:
            return HttpResponse('Указанная директория не существует.', content_type='text/plain; charset=utf-8')

    return render(request, 'management/file_export.html', {'file_contents': file_contents})
