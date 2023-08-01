import json


def add_user_information():
    try:
        with open('result_task2.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    while True:
        name = input("Введите имя пользователя: ")
        id = input("Введите личный идентификатор: ")
        access_level = input("Введите уровень доступа (от 1 до 7): ")

        if int(access_level) < 1 or int(access_level) > 7:
            print("Уровень доступа должен быть от 1 до 7!")
            continue

        # Проверка на уникальность идентификатора
        unique = True
        for users in data.values():
            if id in users:
                unique = False
                print("Идентификатор должен быть уникальным!")
                break

        if not unique:
            continue

        if access_level not in data:
            data[access_level] = {}

        data[access_level][id] = name

        with open('result_task2.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)

        choice = input("Хотите добавить еще пользователя? (да/нет): ")
        if choice.lower() != "да":
            break


add_user_information()
