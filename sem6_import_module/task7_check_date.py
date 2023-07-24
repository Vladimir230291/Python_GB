# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ["check_date"]
def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(date: str) -> bool:
    day, mouth, year = map(int, date.split("."))
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
    print(check_date("29.02.2001"))