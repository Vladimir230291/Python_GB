# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive:
    """Kласс Архив, который хранит пару свойств, число и строку.Паттерн сингтон"""
    _instance = None

    def __init__(self, id_num: int, some_str: str):
        print("init")
        self.id_num = id_num
        self.some_str = some_str

    def __new__(cls, *args, **kwargs):

        """Каждый раз создается один экземпляр меняются только параметры"""
        print("new")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_num = []
            cls._instance.archive_str = []
        else:
            cls._instance.archive_num.append(cls._instance.id_num)
            cls._instance.archive_str.append(cls._instance.some_str)
        return cls._instance


def __str__(self):
    return f"{self.archive_str},{self.archive_num}"


arhc1 = Archive(1, "книга1")
arhc2 = Archive(2, "книга2")
arhc3 = Archive(3, "книга3")

print(arhc1._instance.archive_str)
print(arhc3.id_num, arhc3.some_str)
