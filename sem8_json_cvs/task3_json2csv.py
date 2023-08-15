# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv

__all__ = ["convert_json_to_csv"]


def convert_json_to_csv(json_filename: str) -> None:
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    rows = []
    for access_level, user in data.items():
        for id_user, name in user.items():
            rows.append({"access_level": int(access_level), "id": int(id_user), "name": name})

    name_csv_file = json_filename.split('.')[0] + ".csv"

    with open(name_csv_file, "w", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, fieldnames=["access_level", "id", "name"], dialect="excel-tab")
        dict_writer.writeheader()  # запись заголовков
        dict_writer.writerows(rows)  # запись строк под заголовками
