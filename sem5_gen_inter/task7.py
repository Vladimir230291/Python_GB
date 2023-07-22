# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя»

from itertools import count


def prime_number(n: int):
    gen = (i for i in range(n + 1))
    it_gen = iter(gen)
    while n != 0:
        for i in range(2, n + 1):
            for j in range(2, n):
                pass


prime = prime_number(12)
for i in range(12 - 1):
    print(next(prime))
