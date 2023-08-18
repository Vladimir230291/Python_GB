# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_items_dict(dict_operation: dict, key=None, value=None):
    try:
        tmp = dict_operation.pop(key)
        return dict_operation
    except KeyError as e:
        print(f"такого ключа не существет {e}")
        dict_operation[None] = None



dict_value = {1: 1.1, 2: 2.2, 3: 3.3}
get_items_dict(dict_value, 3, 3)
print(dict_value)
