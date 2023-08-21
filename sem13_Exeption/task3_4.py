# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа

# Задание №6
# 📌 Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода
# проекта.
from task4 import User


class MyException(Exception):
    pass


class ErrorLevel(MyException):
    def __init__(self, user: User, level: int):
        self.user = user
        self.level = level

    def __str__(self):
        return (f'Нельзя добавить пользователя с уровнем {self.level}'
                f'Потому что вы вошли как {self.user.name} с уровнем {self.user.user_level}')


class ErrorAccess(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return (f'Отказанно в доступе!'
                f'Пользователь с именем {self.name} и ID {self.user_id} не найден')