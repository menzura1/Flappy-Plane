import os
import tarfile
from utils import check_files_existence


def create_tar(archive_name, files):
    # Проверяем существование файлов
    check_files_existence(files)

    with tarfile.open(archive_name, "w") as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))  # Сохраняем только имя файла
    print(f"Архив {archive_name} успешно создан.")
