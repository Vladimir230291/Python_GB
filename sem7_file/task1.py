# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MAX_NUM = 1000
MIN_NUM = -1000


def add_random_num_in_file(count_str: int, file_name: str):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(count_str):
            f.write(f"{randint(MIN_NUM, MAX_NUM):>5} | {round(uniform(MIN_NUM, MAX_NUM), 2):>7}\n")


if __name__ == "__main__":
    add_random_num_in_file(5, "/home/user/PycharmProjects/Python_GB/sem7_file/random_num.txt")
