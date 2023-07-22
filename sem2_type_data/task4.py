# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import math
import decimal

decimal.getcontext().prec = 42  # Указываем точность
PI: decimal.Decimal = decimal.Decimal(math.pi)  # Передаем значение пи


def get_number_from_user():
    info = decimal.Decimal((input("Введите диаметр(не больше 1000): ")))
    return info


d = get_number_from_user()
length: decimal.Decimal = d * PI
square = (d / 2) ** 2 * PI
print(length, square, sep="\n")
