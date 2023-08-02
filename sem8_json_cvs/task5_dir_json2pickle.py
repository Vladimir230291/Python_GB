# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import json
import pickle
import os

__all__ = ["pack_file"]

def pack_file(dir_path: str) -> None:
    list_file = filter(lambda list_file: list_file[-5:] == ".json", os.listdir(dir_path))
    for json_file in list_file:
        with open(json_file, 'r', encoding='utf-8') as json_read:
            data = json.load(json_read)
        with open(f'{json_file[:-5]}.pickle', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

