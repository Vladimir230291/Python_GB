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
from typing import Set
from task3_4 import ErrorLevel, ErrorAccess
from task4 import User


class Project:
    def __init__(self, json_file_path: str):
        self.admin_user = None
        self.access_level = None
        self.json_file_path = json_file_path
        self.users = self.load_users()

    def __str__(self):
        return f"{self.users}, {self.admin_user =} {self.access_level =}"

    def load_users(self) -> Set[User]:
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        users_set = set()

        for user in data:
            users_set.add(User(user['name'], user['user_id'], user['access_level']))
        return users_set

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, 0)
        if test_user in self.users:
            for user in self.users:
                if test_user == user:
                    self.admin_user = user
        else:
            raise ErrorAccess(name, user_id)

    def add_user(self, name: str, user_id: int, user_level: int):
        if user_level > self.admin_user.user_level:
            raise ErrorLevel(self.admin_user, user_level)
        new_user = User(name, user_id, user_level)
        self.users.add(new_user)
        self.save_users()

    def save_users(self):
        user_dict = []
        with open(self.json_file_path, 'w', encoding='utf-8') as json_file:
            for user in self.users:
                user_dict.append({"name": user.name, 'user_id': user.user_id, 'access_level': user.user_level})
                print(user)
            json.dump(user_dict, json_file, indent=2, ensure_ascii=False)
            print(user_dict)


if __name__ == '__main__':
    my_project = Project("users.json")
    my_project.entrance("Влад", 4)
    my_project.add_user("Себасътьян", 23, 10)
    print(*my_project.users)
