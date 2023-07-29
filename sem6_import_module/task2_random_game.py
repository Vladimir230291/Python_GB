# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as rd



START = 0
STOP = 30
AMOUNT = 5


def get_random_num(start: int = START, stop: int = STOP, amount: int = AMOUNT):
    """
    Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.

    """
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

    start, stop = map(int, input("Введите начало и конец диапозона числа через пробел: ").split())
    if start < stop:
        if get_random_num(start, stop):
            print("Вы победили")
        else:
            print("Вы проиграли!")
