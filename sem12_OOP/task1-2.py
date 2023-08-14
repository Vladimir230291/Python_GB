# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json


class Factorial:
    """
    Класс для подсчета фокториала числа
    """

    def __init__(self, k):
        self._log_value = {}
        self.list_value = []
        self.k = k

    def __call__(self, value):
        """
        Возвращает значение факториала, и сохраняет ранее вызываемые значения и их факториалы
        :param value: int
        :return: int
        """
        res = 1
        for i in range(1, value + 1):
            res *= i
            self.list_value.append(res)
        self._log_value[value] = res
        self.list_value = self.list_value[-self.k:]
        return self.list_value[-1]

    def view_log(self):
        return self._log_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("task_json.json", "w", encoding="utf-8") as file_json:
            json.dump(self._log_value, file_json)


if __name__ == "__main__":
    f = Factorial(4)
    with f:
        print(f(5))
        print(f(7))
        print(f(10))
        print(f.list_value)
        print(f.view_log())
