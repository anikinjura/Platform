# core/management/utils.py

import os
import logging

def get_files_from_directory(directory, 
                             file_extensions=('.py', '.html', '.css', '.js'),
                             exclude_dirs=('migrations', '__pycache__'),
                             exclude_files=('__init__.py',)):
    """
    Возвращает содержимое всех файлов с указанными расширениями из директории и ее поддиректорий.
    Файлы и директории, которые должны быть исключены, можно задать параметрами.
    
    :param directory: Директория для поиска файлов
    :param file_extensions: Расширения файлов, которые будут выгружаться (по умолчанию: .py, .html, .css, .js)
    :param exclude_dirs: Директории, которые будут исключены из обработки (по умолчанию: migrations, __pycache__)
    :param exclude_files: Файлы, которые будут исключены (по умолчанию: __init__.py)
    :return: Словарь, где ключ - это путь к файлу, а значение - его содержимое
    """
    file_contents = {}

    for root, dirs, files in os.walk(directory):
        # Исключаем указанные директории
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            # Проверяем, чтобы файл подходил по расширению и не был в списке исключенных файлов
            if file.endswith(file_extensions) and file not in exclude_files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        code = infile.read()
                        # Сохраняем содержимое файла в словарь
                        file_contents[file_path] = code
                except Exception as e:
                    # В случае ошибки с чтением файла, просто пропускаем его и добавляем информацию в логи
                    logging.error(f"Ошибка при чтении файла {file_path}: {str(e)}")
                    continue
    
    return file_contents

