# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь

from math import pi


class Circle:
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def circumference(self):
        return pi * pow(self.circle_radius, 2)

    def aria_circle(self):
        return (2 * pi) * self.circle_radius


cir1 = Circle(5)
print(f'{round(cir1.aria_circle(), 2)}, {round(cir1.circumference(), 2)}')
