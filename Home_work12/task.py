# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv
class ValidateName:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, name):
        if name.isalpha() and name[0].isupper():
            setattr(instance, self.name, name)
        else:
            raise ValueError("С большой буквы")


class Student:
    first_name = second_name = last_name = ValidateName()

    def __init__(self, l_name: str, f_name: str, s_name: str, ):
        self.first_name = f_name
        self.second_name = s_name
        self.last_name = l_name
        self.dict_grade = {}
        self.dict_test = {}

    def some_csv_func(self, file_input):
        with open(file_input,"w",encoding="utf-8") as file_csv:
            file_reader = csv.DictReader(file_csv,delimiter=",")
            count = 0
            if count == 0:
                for row in file_reader:

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name} '


if __name__ == '__main__':
