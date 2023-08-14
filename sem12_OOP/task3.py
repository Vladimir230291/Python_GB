# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1

class GenFactorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    @staticmethod
    def calc_fact(number: int):
        res = 1
        for i in range(1, number + 1):
            res *= i
        return res

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            result = self.calc_fact(self.start)
            self.start += self.step
            return result
        raise StopIteration


if __name__ == '__main__':
    fact = GenFactorial(12)
    # for val in fact:
    #     print(val)
    print(next(fact))
    print(next(fact))
    print(next(fact))
    print(next(fact))