import os
import tarfile
from utils import check_file_exists

#список извлечённых файлов
extracted_files = set()


def extract_tar(archive_name,files=None):
    global extracted_files  # используем переменную для хранения извлечённых файлов

    # проверка сущ архива
    check_file_exists(archive_name)

    with tarfile.open(archive_name,"r") as tar:
        archive_files = tar.getnames()  # список всех файлов

        if files is None or not files:  # если архив пустой извлекаем все
            tar.extractall()
            print(f"Все файлы из архива {archive_name} извлечены.")
        else:
            for file in files:
                if file in archive_files:
                    if file not in extracted_files:
                        tar.extract(file)
                        extracted_files.add(file)  # добавление файла в уже извлеч файлы
                        print(f"Файл {file} извлечен.")

                        # проверка на директорию
                        if os.path.isdir(file):
                            # если это папка извлекаем все её содержимое
                            print(f"Папка {file} извлечена с содержимым.")
                            for member in tar.getmembers():
                                if member.name.startswith(file):  # все файлы внутри папки
                                    if member.name not in extracted_files:
                                        tar.extract(member)
                                        extracted_files.add(member.name)
                                        print(f"Файл {member.name} извлечен из папки {file}.")
                    else:
                        print(f"Файл {file} уже извлечен.")
                else:
                    print(f"Ошибка: Файл {file} не найден в архиве {archive_name}.")
