# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

__all__ = ["group_rename_files"]

import os


def group_rename_files(end_name: str, num_digits: int, source_ext: str, ext_file_end: str,
                       name_range: list, dir: str) -> None:
    """
    Групповое переименование файлов.
    :param
    - end_name (str): Желаемое конечное имя файлов.
    - num_digits (int): Количество цифр в порядковом номере.
    - source_ext (str): Расширение исходного файла.
    - ext_file_end (str): Расширение конечного файла.
    - name_range (list): Диапазон сохраняемого оригинального имени.
    - dir (str): Директория с которой надо работать.
    """
    files = os.listdir(dir)  # список файлов в директории
    print(files)
    counter = 1

    for file in files:
        if file.endswith(source_ext):  # проверяем расширение исходного файла
            original_name = file[name_range[0] - 1:name_range[1]]  # берем диапазон символов из оригинального имени
            new_name = original_name + end_name + str(counter).zfill(num_digits)  # создаем новое имя файла
            new_name_with_extension = new_name + ext_file_end  # добавляем расширение конечного файла
            os.rename(os.path.join(dir, file),
                      os.path.join(dir, new_name_with_extension))  # переименовываем файл

            counter += 1


if __name__ == "__main__":
    group_rename_files("_new", 3, ".txt",
                       ".docx", [3, 6], "/home/user/PycharmProjects/Python_GB/Home_work7")
