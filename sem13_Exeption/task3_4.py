# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа


class MyException(Exception):
    pass


class ErrorLevel(MyException):
    pass


class ErrorAccess(MyException):
    pass
