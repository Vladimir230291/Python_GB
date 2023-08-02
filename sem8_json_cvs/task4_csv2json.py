# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json

__all__ = ["csv2json"]
def csv2json(csv_file_path: str, json_file_path: str) -> None:
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        data_csv_rows = csv.reader(f, dialect="excel-tab")
        data = []
        for i, row in enumerate(data_csv_rows):
            if i:
                access_level, user_id, name = row
                user_data = {}
                user_data["access_level"] = int(access_level)
                user_data["user_id"] = f'{int(user_id):010}'
                user_data["name"] = name.capitalize()
                user_data["hash"] = hash((user_id, name))
                data.append(user_data)
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



