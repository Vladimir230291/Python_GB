# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, a: int, b: int = None):  # a & b стороны прямоугольника
        self._a = a
        self._b = a if b is None else b

    def perimeter(self):
        return (self._a + self._b) * 2

    def square(self):
        return self._a * self._b


r = Rectangle(43)

print(r.perimeter(), r.square())
