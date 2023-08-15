import csv

# Открываем файл CSV
with open('table.csv', 'r', encoding="utf-8") as file:
    # Создаем объект DictReader
    csv_reader = csv.DictReader(file)

    # Создаем словарь
    data_list = []

    # Читаем каждую строку CSV и добавляем значения в словарь
    for row in csv_reader:
        data_list.append(row)

# Выводим содержимое словаря
print("____")
print(data_list[0].keys())
