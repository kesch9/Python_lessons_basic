# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)

    def area(self):
        # Площадь треугольника по формуле Герона
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def height(self):
        return (2 * Triangle.area(self)) / self.a

    def perimetr(self):
        return self.a + self.b + self.c

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Теперь попробуем передать кортежем
class Isosceles_trapezoid:

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # вычислим длины сторон и сохраним в словарь
        self.__dict_length = {'AB': sqrt((self.A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2),
                   'BC': sqrt((B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2),
                   'CD': sqrt((C[0] - D[0]) ** 2 + (C[1] - D[1]) ** 2),
                   'DA': sqrt((D[0] - A[0]) ** 2 + (D[1] - A[1]) ** 2)}
    # проверка
    def is_isosceles(self):
        if self.__dict_length['BC'] != self.__dict_length['DA'] :
            return "Трапеция не равнобокая"
        else:
            return "Трапеция равнобокая"

    # длины сторон
    def length(self):
        return self.__dict_length

    # периметр
    def perimetr(self):
        return self.__dict_length['AB'] + self.__dict_length['BC'] + \
               self.__dict_length['CD'] + self.__dict_length['DA']

    # площадь
    def square(self):
        h = sqrt(self.__dict_length['AB'] ** 2 -
                 (((self.__dict_length['DA'] - self.__dict_length['BC']) ** 2 + self.__dict_length['AB'] ** 2 - self.__dict_length['CD'] ** 2) /
                  2 * (self.__dict_length['DA'] - self.__dict_length['BC'])) ** 2)
        return (self.__dict_length['BC'] + self.__dict_length['DA']) * h / 2




if __name__ == "__main__":
    print("#"*30)
    triangle = Triangle(1,2,3,4,5,6)
    print(f"Площадь {triangle.area()}")
    print(f"Высота {triangle.height()}")
    print(f"Периметр {triangle.perimetr()}")
    print("#" * 30)
    trapezoid = Isosceles_trapezoid((1, 1), (5, 1), (4, 4), (2, 4))
    print(trapezoid.is_isosceles())
    print(trapezoid.length())
    print(trapezoid.perimetr())
    print(trapezoid.square())