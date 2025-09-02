import os
import tarfile
from utils import check_files_existence


def create_tar(archive_name, files):
    # проверка существования файлов
    check_files_existence(files)

    # создание архива
    with tarfile.open(archive_name, 'w') as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))  # добавляем файл в архив
    print(f'Архив {archive_name} успешно создан')
