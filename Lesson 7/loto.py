#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
def soft_to_max(origin_list, start, end):
    for i in range(end, start, end, -1):
        for j in range(start , i):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1] , origin_list [j]
# карточка
class Card():
    def __init__(self):
        # Количество строк в карточке
        self._row_count = 3
        # кол-во столбцов в карточке
        self._column_count = 9
        # кол-во необходимых чисел в строке
        self._number_in_row_count = 5
        # создаем список из 15 чисел с нумерацией от 1 до 91
        self._numbers = random.sample(range(1,91),15)
        # Кол-во вытащенных боченков
        self._kegs_count = 15
        # список позиций (0-8) в карточке для расстоновки чисел
        self._distribution_row = list()
        #  Перебираем каждую из трех строчек (i = 0,1,2)
        for i range(self._row_count):
            print(self._numbers_in_row_count * i)
            # вызываем функцию сортировки чисел карточки по возрастания
            # передаем в функцию 15 чисел карточки
            # указываем что сортируем первые пять чисел карточки, потом вторые пять, потом третьи пять
            # self._number_in_row_count * i = 0
            # self._number_in_row_count * (i+1) - 1 = 4 итд
            sort_to_max (self._numbers, self._number_in_row_count * i, self._number_in_row_count *(i+1)-1)
            # добавляем позиции чисел в карточке
            # позиции от 0 до 8, добавляем по 5 позиций на каждом шаге цикла (при переходе на очередную строку)
            self._distribution_row += random.sample(range(self._column_count), self._number_in_row_count)
