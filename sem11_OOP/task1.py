# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime
import time


class MyString(str):
    """Класс хранит в себе какой-нибудь текст, автора текста, и время написания текста"""

    def __new__(cls, my_str, autor_name):
        """Добавляется текст и автор, записывается время создания класса"""
        _instance = super().__new__(cls, my_str)
        _instance.autor_name = autor_name
        _instance.time_create = datetime.time(datetime.now()).strftime('%H:%M:%S')

        return _instance


if __name__ == "__main__":
    # print(help(MyString))
    some_string = MyString("Сторока", "Владимир")
    time.sleep(1)
    some_string_1 = MyString("Еще одна строка", "Автор")

    print(MyString.__doc__)
    print(some_string.__doc__)
    print(some_string.__new__.__doc__)
