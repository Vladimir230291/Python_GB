# Задание №1
# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename="log.log", encoding='utf-8', level=logging.ERROR)


def division(a: int, b: int) -> float:
    result = None
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"Деление на ноль! {e}")
        result = float("inf")
    return result

if __name__ == '__main__':
    print(division(12, 3))
    print(division(12, 0))
