# Задание №6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера

class Descr:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError("Отрицательное нельзя")


class Rectangle:
    a = Descr()
    b = Descr()

    def __init__(self, a: int, b: int = None):  # a & b стороны прямоугольника
        self.a = a
        self.b = a if b is None else b

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b

    def __str__(self):
        return f"{self.a, self.b}"


if __name__ == '__main__':
    r = Rectangle(1, 3)

    print(r.square())
