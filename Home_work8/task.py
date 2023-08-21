# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий

import os
import json
import csv
import pickle


def dir_recursive_walk(directory):
    dir_info = []

    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.basename(os.path.abspath(root))
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            dir_info.append({'path': file_path, 'type': 'file', 'size': file_size, 'parent_dir': parent_dir})

        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size += sum(os.path.getsize(os.path.join(dir_path, file)) for file in os.listdir(dir_path))

            dir_info.append({'path': dir_path, 'type': 'directory', 'size': dir_size, 'parent_dir': parent_dir})

    # сохранение в json
    with open('dir_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(dir_info, json_file, ensure_ascii=False, indent=2)

    # сохранение в csv
    with open('dir_info.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['path', 'type', 'size', 'parent_dir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect="excel-tab")
        writer.writeheader()
        writer.writerows(dir_info)

    # сохранение в pickle
    with open('dir_info.pickle', 'wb') as pickle_file:
        pickle.dump(dir_info, pickle_file)


if __name__ == "__main__":
    dir_recursive_walk('/home/users/PycharmProjects/Python_GB')
