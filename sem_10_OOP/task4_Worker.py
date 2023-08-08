# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task3_Human import Human


class Worker(Human):

    def __init__(self, id_num: str, first_name, last_name, second_name, age: int, phone_number):
        super().__init__(first_name, last_name, second_name, age, phone_number)

        self.id_num = id_num if id_num.isdigit() and len(id_num) == 6 else None  # проверка корректности
        self.__lvl_access = sum([int(n) for n in id_num]) % 7  # вычисление уровня доступа

    def check_access_lvl(self):
        return self.__lvl_access


w = Worker("124578", "Первое", "Последнее", "Второе", 22, "112")
print(w.full_name())
print(w.check_access_lvl())
