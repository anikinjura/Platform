import os

def extract_code_from_files(directory, output_file, 
                            file_extensions=('.py', '.html', '.css', '.js'),
                            exclude_dirs=('migrations', '__pycache__'),
                            exclude_files=('__init__.py',)):
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            # Исключаем директории
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.endswith(file_extensions) and file not in exclude_files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        code = infile.read()
                        # Запись кода в файл
                        outfile.write(f"### Код из файла: {file_path} ###\n")
                        outfile.write(code)
                        outfile.write("\n" + "#" * 80 + "\n\n")  # Разделитель между файлами

# Пример использования:
directory_path = "C:/Users/y.ank/dev/Platform/core"  # Укажи путь к своему проекту
output_file = "C:/Users/y.ank/dev/Platform/platform_base/extracted_code.txt"  # Укажи путь к файлу, куда сохранить код
extract_code_from_files(directory_path, output_file)

print(f"Код всех файлов из {directory_path} был успешно выгружен в {output_file}.")
