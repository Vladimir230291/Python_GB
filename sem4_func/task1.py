# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def print_sort_text(text: list):
    text.sort()
    max_len = 0
    for word in text:
        if len(word) > max_len:
            max_len = len(word)
    for num, word in enumerate(text, start=1):
        print(f"{num}. {word:>{max_len}}") #выравнивание длине


text = input("Введите текст: ").split()
print_sort_text(text)
