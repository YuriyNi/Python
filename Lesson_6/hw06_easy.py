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
        self.AB = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        self.BC = math.sqrt((self.x2-self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        self.AC = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)

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

class Trapeze:
    def __init__(self, A, B, C, D):

        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA


        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)

    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False