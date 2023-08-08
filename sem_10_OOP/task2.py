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
        self.a = a
        self.b = a if b is None else b

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b


r = Rectangle(43)

print(r.perimeter(), r.square())
