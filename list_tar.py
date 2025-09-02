import tarfile

def list_tar(archive_name):
    try:
        with tarfile.open(archive_name, "r") as tar:
            print(f"Содержимое архива {archive_name}:")
            for member in tar.getmembers():
                print(f"- {member.name}")  # вывод имени каждого файла в архиве
    except FileNotFoundError:
        print(f"Ошибка: Архив {archive_name} не найден.")
    except tarfile.TarError:
        print(f"Ошибка: Не удается открыть архив {archive_name}. Возможно, это поврежденный архив.")
