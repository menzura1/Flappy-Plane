import sys
import os
import argparse
from create_tar import create_tar
from extract_tar import extract_tar
from list_tar import list_tar  # Новый импорт для функции списка


def main():
    parser = argparse.ArgumentParser(description="Сделать архив или извлечь файлы.")
    parser.add_argument("-f", "--file", help="Имя архива", required=True)
    parser.add_argument("-x", "--extract", help="Извлечь файлы из архива", action="store_true")
    parser.add_argument("-a", "--all", help="Извлечь все файлы из архива",
                        action="store_true")  # Флаг для извлечения всех файлов
    parser.add_argument("-l", "--list", help="Просмотреть содержимое архива",
                        action="store_true")  # Новый флаг для просмотра архива
    parser.add_argument("files", nargs="*", help="Файлы для архивации или извлечения")

    args = parser.parse_args()

    if args.list:  # Если флаг --list, вызываем функцию для вывода содержимого архива
        list_tar(args.file)
    elif args.extract:
        if args.all:  # Если флаг --all указан, извлекаем все файлы
            extract_tar(args.file)
        elif not args.files:
            print("Ошибка: нужно указать файлы для извлечения из архива.")
            sys.exit(1)
        else:
            extract_tar(args.file, args.files)
    else:
        if not args.files:
            print("Ошибка: нужно указать файлы для архивации.")
            sys.exit(1)
        create_tar(args.file, args.files)


if __name__ == "__main__":
    main()
