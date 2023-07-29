# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало

from typing import TextIO


def read_file(url1: str, url2: str, res_url: str):
    with (
        open(url1, "r", encoding="utf-8") as f_num,
        open(url2, "r", encoding="utf-8") as f_name,
        open(res_url, "w", encoding="utf-8") as result
    ):
        len_names = len(f_name.readlines())
        len_num = len(f_num.readlines())
        for _ in range(max(len_names, len_num)):
            name = readline_or_begin(f_name)
            num1, num2 = readline_or_begin(f_num).split("|")
            math = int(num1) * float(num2)

            if math < 0:
                result.write(f"{name.upper()} | {round(math)}\n")
            else:
                result.write(f"{name.lower()} | {abs(math)}\n")


def readline_or_begin(file: TextIO) -> str:
    text = file.readline()
    if text == '':
        file.seek(0)
        text = file.readline()
    return text[:-1]


read_file("/home/user/PycharmProjects/Python_GB/sem7_file/random_num.txt",
          "/home/user/PycharmProjects/Python_GB/sem7_file/random_name.txt",
          "/home/user/PycharmProjects/Python_GB/sem7_file/result.txt")
