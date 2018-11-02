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


import os
import sys

_ = ("1.Перейти в папку" , "2.Просмотреть содержимое текущей папки", "3.Удалить папку", "4.Создать папку - make_Dir")
for i in _:
    print(i)

comands = input("Введите команду:")

print('sys.argv = ', sys.argv)

def print_help():
    print("papka - Перейти в папку")
    print("sodpapka - Посмотреть содержимое папки")
    print("delpapka - Удалить папку")
    print("mkdir <dir_name> - создание директории")

def make_Dir():
    from hw05_easy import make_dir
    return make_Dir()



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














