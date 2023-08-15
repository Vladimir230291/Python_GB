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
    """
    Класс который берет данные из csv файла(оценки и баллы) и выводит на печать всю информацию по успеваемости.
    """
    first_name = ValidateName()
    second_name = ValidateName()
    last_name = ValidateName()
    _middle_score = {}

    def __init__(self, l_name: str, f_name: str, s_name: str):
        self.first_name = f_name
        self.second_name = s_name
        self.last_name = l_name
        self.list_result = self.read_csv(f"{l_name}{f_name}{s_name}.csv")
        self._middle_score = self.middle_score()
        self._all_middle_grades = self._middle_grade()

    @staticmethod
    def read_csv(file_input):
        with open(file_input, "r", encoding="utf-8") as file_csv:
            file_reader = csv.DictReader(file_csv, delimiter=",")
            res_list = []
            for val in file_reader:
                res_list.append(val)

        return res_list

    def print_list_score(self):
        for val in self.list_result:
            print(val)

    # Средний балл
    def middle_score(self):
        for dict_value in self.list_result:
            grades = sum(map(int, dict_value["оценки"].split(','))) / len(dict_value["оценки"].split(','))
            score = sum(map(int, dict_value["баллы"].split(','))) / len(dict_value["баллы"].split(','))
            self._middle_score[dict_value["предмет"]] = {"средняя оценка": grades, "средний балл": round(score)}

        return self._middle_score

    # средняя оценка по всем предметам вместе взятых
    def _middle_grade(self):
        tmp_list = []
        for key, grade in self._middle_score.items():
            tmp_list.append(grade["средняя оценка"])
        return round(sum(tmp_list) / len(tmp_list), 1)

    def __str__(self):
        return (f"Студент: {self.last_name} {self.first_name} {self.second_name}\n"
                f"Имеет следующие оценки и баллы: \n"
                f"{self.list_result}\n"
                f"Cредний балл: \n"
                f"{self._middle_score}\n"
                f"Средний общий балл по всем предметам:\n"
                f"{self._all_middle_grades}\n"
                f"{'__' * 10}\n")


if __name__ == '__main__':
    st1 = Student("Гаврилов", "Вячеслав", "Николаевич")
    st2 = Student("Иванов", "Владимир", "Петрович")
    print(st1, st2)
