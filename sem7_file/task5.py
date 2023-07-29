# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи
from string import ascii_lowercase, digits
from random import choices, randint


def make_files(f_ext: str, min_len_name: int = 6, max_len_name: int = 30,
               min_bite: int = 256, max_bite: int = 4096, count_file: int = 42) -> None:
    for _ in range(count_file):
        name = "".join(choices(ascii_lowercase + digits + "_", k=randint(min_len_name, max_len_name)))
        data_bytes = bytes(randint(0, 255) for _ in range(randint(min_bite, max_bite)))
        with open(rf"file_for_task4/{name}.{f_ext}", "wb") as f:
            f.write(data_bytes)


def many_extensions(**kwargs):
    for ext, count in kwargs.items():
        make_files(ext, count_file=count)


many_extensions(txt=3, jpeg=7)
