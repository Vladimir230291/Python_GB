# задание 7
# Не используюя для cvs DictWriter
import csv
import json
import pickle

__all__ = ["cvs2pickle_print"]

def cvs2pickle_print(csv_file_path: str) -> None:
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, dialect="excel")
        list_row = []
        headers = []
        for i, row in enumerate(reader):
            if not i:
                headers = row
            else:
                row_data = {key: val for key, val in zip(headers, row)}
                list_row.append(row_data)
        print(pickle.dumps(list_row))

