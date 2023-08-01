# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def convert_json_to_csv(json_filename: str):
    try:
        with open(json_filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {json_filename} не найден.")
        return

    # замена формата фойла
    csv_filename = json_filename.split(".")[0] + ".csv"

    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())

    print(f"Содержимое файла {json_filename} успешно сохранено в {csv_filename} в формате CSV.")


convert_json_to_csv("result_task2.json")
