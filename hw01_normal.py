



__author__ = 'Ни Юрий Олегович'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Число приходит в виде целого беззнакового.


x = (input("Введите целое произвольное число"))
print (max(x))

""""
мой вариант 2
x = (input("Введите целое произвольное число"))
l = list (str(x))
list = (max (l))
list2 = int (list)
print (abs(list2))

"""

# Задача-2: Запросить у пользователя два целых числа, связать их с переменными.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.


a = int(input("Введите целое число а: "))
b = int(input("Введите целое число b: "))
a,b = b,a
print("a = ", a, "b = ", b)







# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

print ('Привет, эта программа вычисляет корни квадратного уравнения типа: ax2 + bx + c = 0 ')
import math
a = int(input("Введи значения a:"))
b = int(input("Введи значения b:"))
c = int(input("Введи значения c:"))
d = b**2 - 4*a*c
if d < 0:
    print ("корней нет")
elif d == 0:
    x1 = (-b + math.sqrt (d))/2*a
    print ("x1=",x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / 2*a
    x2 = (-b -(math.sqrt(d)))/2*a
    print ("x1=",x1 , "x2=",x2)



