# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.

# Задание №5
# 📌 Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.
import sys
class Rectangle:
    __slots__ = ("__a", "__b")

    def __init__(self, a: int, b: int = None):  # a & b стороны прямоугольника
        self.__a = a
        self.__b = a if b is None else b

    @property
    def a(self, value):
        if value > 0:
            return self.__a
        else:
            raise ValueError("Отрицательное число")

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value > 0:
            self.__b = value

    def perimeter(self):
        return (self.__a + self.__b) * 2

    def square(self):
        return self.__a * self.__b

    def __str__(self):
        return f"{self.__a, self.__b}"


if __name__ == '__main__':
    rect = Rectangle(4, 3)
    rect.a = 2
    print(sys.getsizeof(rect))
    print(dir(rect))
