# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """Kласс Архив, который хранит пару свойств, число и строку.Паттерн сингтон"""

    _instance = None

    def __init__(self, id_num: int, some_str: str):

        self.id_num = id_num
        self.some_str = some_str

    def __new__(cls, *args, **kwargs):

        """Каждый раз создается один экземпляр меняются только параметры"""


        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_num = []
            cls._instance.archive_str = []
        else:
            cls._instance.archive_num.append(cls._instance.id_num)
            cls._instance.archive_str.append(cls._instance.some_str)
        return cls._instance

    def __str__(self):
        return (f"Текстовое значение: {self.id_num} цифровое значение: {self.some_str}\n"
                f"Archive of text: {self.archive_str}\n"
                f"Archive of num: {self.archive_num}")

    def __repr__(self):
        return f'num: {self.id_num}, text: {self.some_str}'


arhc1 = Archive(1, "книга1")
arhc2 = Archive(2, "книга2")
arhc3 = Archive(3, "книга3")

print(arhc1)
print(repr(arhc1))