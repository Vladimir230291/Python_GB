# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def my_get(my_dict, key, default: int | float = None) -> int | float | None:
    result = default
    try:
        result = my_dict[key]
    except KeyError as e:
        pass
    return result


dict_value = {1: 1.1, 2: 2.2, 3: 3.3}

print(my_get(dict_value, 4, "Пусто"))
