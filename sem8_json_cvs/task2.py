import json
import os.path


def add_user_information(json_file):
    user_ids = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for user in data.values():
                user_ids.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input("Введите имя пользователя: ")
        if not name:
            break

        id_user = input("Введите личный идентификатор: ")
        if id_user in user_ids:
            print("Такой id есть!")
            continue

        access_level = input("Введите уровень доступа (от 1 до 7): ")
        if int(access_level) < 1 or int(access_level) > 7:
            print("Уровень доступа должен быть от 1 до 7!")
            continue

        data[access_level][id_user] = name

        with open(json_file, 'w',encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False, sort_keys=True)

        choice = input("Хотите добавить еще пользователя? (да/нет): ")
        if choice.lower() != "да":
            break


add_user_information("result_task2.json")
