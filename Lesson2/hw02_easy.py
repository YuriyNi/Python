

__author__ = 'Ни Юрий Олегович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


print ("Привет, эта программа выводит список фруктов в виде нумерованного списка, \
выровненного по правой стороне ")
list =  ["яблоко", "банан", "киви", "арбуз"]
print ("1. {:>10}".format(list[0]))
print ("2. {:>10}".format(list[1]))
print ("3. {:>10}".format(list[2]))
print ("4. {:>10}".format(list[3]))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.

list = [1,2,3]
list2 = [1,3,4,5]
print (set(list + list2))



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

list = [1,2,3,4,5,6,7,8,9]
new_list = []
for i in list:
    if i %  2 == 0:
      new_list.append (i/4)
    else:
        new_list.append (i*2)
print (new_list)

