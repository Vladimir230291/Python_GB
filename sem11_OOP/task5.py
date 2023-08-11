# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.

# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения


from sem_10_OOP.task2 import Rectangle


class RectanglePro(Rectangle):
    """
    Класс прямоугольник, который можно сравнивать по площади
    """

    def __add__(self, other: Rectangle):
        """
        Метод вычисляет сумму периметра прямоугольников
        """
        sum_of_perims = self.perimeter() + other.perimeter()
        side_a = self.a + other.b
        side_b = sum_of_perims / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __sub__(self, other):
        """
        Метод для вычитания периметров прямоугольников
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        diff = self.perimeter() - other.perimeter()
        side_a = abs(self.a - self.b)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __le__(self, other):
        return self.square() <= other.square()
