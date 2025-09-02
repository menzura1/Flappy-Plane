import os
import tarfile
from utils import check_file_exists

# Список извлечённых файлов в рамках текущего сеанса
extracted_files = set()


def extract_tar(archive_name, files=None):
    global extracted_files  # Используем глобальную переменную для хранения извлечённых файлов

    # Проверяем существование архива
    check_file_exists(archive_name)

    with tarfile.open(archive_name, "r") as tar:
        archive_files = tar.getnames()  # Получаем список всех файлов в архиве

        if files is None or not files:  # Если не указаны файлы или список пуст, извлекаем все
            tar.extractall()
            print(f"Все файлы из архива {archive_name} извлечены.")
        else:
            for file in files:
                if file in archive_files:
                    if file not in extracted_files:
                        tar.extract(file)
                        extracted_files.add(file)  # Добавляем файл в множество извлечённых
                        print(f"Файл {file} извлечен.")
                    else:
                        print(f"Файл {file} уже извлечен.")
                else:
                    print(f"Ошибка: Файл {file} не найден в архиве {archive_name}.")
