__author__ = 'Ни Юрий Олегович'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

""""
number = int (input ("Введите произвольное целое число:  "))
l=list(str(number))
i = 0
while i < len (l):
    print (l[i])
    i += 1
"""



# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a = input("Введите число a:  ")
b = input ("Введите число b:   ")
c = a
a = b
b = c

print (" a = ", a)
print (" b = ", b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

answer = int(input("Сколько вам лет? "))
if answer >= 18:
    print ("Доступ разрешен")
else:
    print ('Извините, пользование данным ресурсом только с 18 лет')