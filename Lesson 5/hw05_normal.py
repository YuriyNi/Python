# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# К сожалению не успел закончить (

import os
import sys
from hw05_easy import make_dir , del_dir
print('sys.argv = ', sys.argv)


main= ("Перейти в папку - 1", "Просмотреть содержимое текущей папки- 2", "Удалить папку - 3", "Создать папку - 4")
for _ in main:
    print(_)



comands = input("Введите команду:")

if comands == "1":
    print(1)

elif comands == "2":
    print(os.listdir())

elif comands == "3":
    del_name = input("Введите название папки для удаления")
    if del_dir (del_name):
        print("{} Дирректория удалена".format(del_name))




elif comands == "4":
    dir_name = input("Введите название дирректории")
    if make_dir(dir_name):
        print("{} Дирректория создана".format(dir_name))


"""

def print_help():
    print("papka - Перейти в папку")
    print("sodpapka - Посмотреть содержимое папки")
    print("delpapka - Удалить папку")
    print("mkdir <dir_name> - создание директории")





def - "Перейти в папку ????????????????"




def sod_dir():
    print(os.listdir())
    return sod_dir()


do = {
    "papka": ,  #Перейти в папку
    "sodpapka": sod_dir,
    "delpapka": del_dir,
    "mkdir": make_Dir,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


"""











