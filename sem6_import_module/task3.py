# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint as rd
from sys import argv

"""
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.

"""
__all__ = ["get_random_num"]
START = 0
STOP = 30
AMOUNT = 5


def get_random_num(start: int = START, stop: int = STOP, amount: int = AMOUNT):
    rand_num = rd(start, stop)
    while AMOUNT > 0:
        print(f"Количество попыток: {amount}")
        user_num = int(input("Введите число: "))
        if user_num == rand_num:
            return True
        elif user_num < rand_num:
            print("Больше!")
        else:
            print("Меньше!")
        amount -= 1
        if amount == 0:
            return False


if __name__ == "__main__":
    name, *param = argv
    if get_random_num(*(int(elem) for elem in param)):
        print("Вы победили")
    else:
        print("Вы проиграли!")
