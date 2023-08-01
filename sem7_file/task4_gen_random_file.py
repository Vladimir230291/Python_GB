# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

__all__ = ["make_files"]
from string import ascii_lowercase, digits
from random import choices, randint


def make_files(f_ext: str, min_len_name: int = 6, max_len_name: int = 30,
               min_bite: int = 256, max_bite: int = 4096, count_file: int = 42) -> None:
    for _ in range(count_file):
        name = "".join(choices(ascii_lowercase + digits + "_", k=randint(min_len_name, max_len_name)))
        data_bytes = bytes(randint(0, 255) for _ in range(randint(min_bite, max_bite)))
        with open(rf"file_for_task4/{name}.{f_ext}", "wb") as f:
            f.write(data_bytes)

#
# if __name__ == "__main__":
#