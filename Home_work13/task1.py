# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.


def get_num(text: str = None):

    while True:
        num = input(text)
        try:
            data = float(num)
            break
        except ValueError as e:
            print("введите число")

    return data


print(get_num("enter: "))