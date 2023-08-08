# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

__all__ = ["Human"]

class Human:
    def __init__(self, first_name, last_name, second_name, age: int, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.second_name = second_name
        self.__age = int(age)
        self.phone_number = phone_number

    def birthday(self):
        self.__age += 1

    def full_name(self) -> str:
        return (f'{self.last_name} {self.first_name} {self.second_name}\n'
                f'номер телефона: {self.phone_number}\n'
                f'Возраст: {self.__age}')



if __name__ == "__main__":
    h = Human("Имя", "Фамилия", "Отчество", 21, "89618887878")
    print(h.full_name())
    h.birthday()
    h.birthday()
    print(h.full_name())


