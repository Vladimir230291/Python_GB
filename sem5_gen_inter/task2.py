# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

from itertools import islice

text = "Некоторые языки программирования накладывают ограничения на максимальную длину строки," \
       " но в большинстве языков подобные ограничения отсутствуют"

res_dict = {ch: ord(ch) for ch in text}
print(res_dict)

# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

dict_it = iter(res_dict.items())
print(*islice(dict_it, 5),sep="\n")
