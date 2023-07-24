# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(day: int, mouth: int, year: int) -> bool:
    if not (0 < day <= 31 and 1 <= mouth <= 12 and 1 <= year <= 9999):
        return False
    if mouth in (4, 6, 9, 11) and day > 30:
        return False
    if mouth == 2 and day > 29 and if_leap(year):
        return False
    if mouth == 2 and day > 28 and not if_leap(year):
        return False
    return True


if __name__ == "__main__":
    name, *param = argv
    if check_date(*(int(item) for item in param)):
        print("Такая дата существует")
    else:
        print("Даты не существет")
