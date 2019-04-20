# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

from os import path, mkdir, rmdir, getcwd, listdir
from sys import argv
from shutil import copyfile


def create_dir(name):
    dir_path = path.join(getcwd(), name)
    try:
        mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')


def delete_dir(name):
    dir_path = path.join(getcwd(), name)
    try:
        rmdir(dir_path)
    except FileNotFoundError:
        print("Такой директории нет")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def dir_view():
    for dir_name in listdir(getcwd()):
        if path.isdir(dir_name):
            print(dir_name)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    copyfile(argv[0], argv[0] + "_copy")


if __name__ == "__main__":
    for i in range(9):
        create_dir('dir_' + str(i + 1))
    for i in range(9):
        delete_dir('dir_' + str(i + 1))
    dir_view()
    copy_file()
