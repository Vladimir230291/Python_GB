# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

some_tuple = (2, 6.4, "string", True, None, 13, "some", False)
res_dict = {}
for value in some_tuple:
    if type(value) in res_dict.keys():
        res_dict[type(value)].append(value)
