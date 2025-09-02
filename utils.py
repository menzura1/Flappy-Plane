import os

def check_files_existence(files):
    for file in files:
        if not os.path.exists(file):
            print(f"Ошибка: Файл {file} не найден.")
            exit(1)

def check_file_exists(file):
    if not os.path.exists(file):
        print(f"Ошибка: Архив {file} не существует.")
        exit(1)
