# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

__all__ = ["gen_name"]

import random


def gen_name() -> str:
    vowels = ["a", "e", "i", "o", "u", "y"]

    length = random.randint(4, 7)
    first_vowel_index = random.randint(0, len(vowels) - 1)

    name = vowels[first_vowel_index].upper()
    while len(name) < length:
        if name[-1] in vowels:
            consonants = [chr(i) for i in range(ord("a"), ord("z") + 1) if chr(i) not in vowels]
            random_consonant = random.choice(consonants)
            name += random_consonant
        else:
            random_vowel = random.choice(vowels)
            name += random_vowel

    with open("random_name.txt", "a", encoding="utf-8") as f:
        print(name, file=f)

#
# def write_in_file(text: str):
#     with open("random_name.txt", "a", encoding="utf-8") as f:
#         print(text, file=f)



