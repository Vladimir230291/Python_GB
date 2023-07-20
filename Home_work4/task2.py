# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def keyword_args_to_dict(**kwargs):
    res_dict = {}
    for val, key in kwargs.items():
        try:
            tmp = hash(key)
        except TypeError:
            key = str(key)
        res_dict[key] = val
    return res_dict


print(keyword_args_to_dict(имя=[56, 0], имя2="значение"))
