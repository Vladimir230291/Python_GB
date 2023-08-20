# Задание №5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json

from task4 import User


class Project:
    def __init__(self, users: set[User], admin_user: User, json_file_path: str):
        self.users = users
        self.admin_user = admin_user
        self.json_file_path = json_file_path

    def load_users(self) -> set[set[User]]:
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        users_set = set()

        for users in data:
            users_set.add(User(users['name'], users['user_id'], users['access_level']))
        return users_set
