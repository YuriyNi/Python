# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Tetra:
    def __init__(self, x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3



    def AB(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

    def BC(self):
        return math.sqrt((self.x2-self.x3)** 2 + (self.y2 - self.y3) ** 2)

    def AC(self):
        return math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)

    def perimeter(self):
        return self.AB + self.BC + self.AC


    def square (self):
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    def height(self):
        return self.square() / (self.AB / 2)









# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

