# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

__all__ = ["create_random_file"]

import os
from string import ascii_lowercase, digits
from random import choices, randint
from os import path


def create_random_file(dir, **kwargs) -> None:
    if not path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    many_extensions(**kwargs)


def make_files(f_ext: str, min_len_name: int = 6, max_len_name: int = 30,
               min_bite: int = 256, max_bite: int = 4096, count_file: int = 42,
               ) -> None:
    for _ in range(count_file):
        name = "".join(choices(ascii_lowercase + digits + "_", k=randint(min_len_name, max_len_name)))
        data_bytes = bytes(randint(0, 255) for _ in range(randint(min_bite, max_bite)))

        with open(rf"{name}.{f_ext}", "wb") as f:
            f.write(data_bytes)


def many_extensions(**kwargs):
    for ext, count in kwargs.items():
        make_files(ext, count_file=count)



