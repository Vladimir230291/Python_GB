# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.
import json
from typing import List, Set

from task3_4 import ErrorLevel, ErrorAccess


class User:
    def __init__(self, name: str, user_id: int, user_level: int):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __str__(self):
        return f'{self.name = }, {self.user_id = }, {self.user_level = }'


def load_users(json_file_path: str) -> set[set[User]]:
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    users_set = set()

    for users in data:
        users_set.add(User(users['name'], users['user_id'], users['access_level']))
    return users_set


if __name__ == '__main__':
    print(*load_users('users.json'), sep='\n')
