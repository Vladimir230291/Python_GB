# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def list_unicode(text: str) -> list:
    list_res = []
    # text_split = list(text.replace(" ", ""))
    for ch in text:
        list_res.append(ord(ch))
    return sorted(list_res)

print(list_unicode("какой то текст"))