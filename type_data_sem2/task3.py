# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.

DIVIDERS = (2, 8)


def get_number_from_user() -> tuple[int, int]:
    num, div = map(int, input("Введите число и делитель: ").split())
    return num, div


def convert_int(number: int, divider: int):
    r: str = ""
    while number > 0:
        r = str(number % divider) + r
        number //= divider
    return number


number, divider = get_number_from_user()
if type(number) == int and divider in DIVIDERS:
    print(convert_int(number, divider))
else:
    print("Еще раз")
