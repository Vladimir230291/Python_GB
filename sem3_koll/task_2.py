# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

some_text = input("data: ")
res = None

if some_text.isdecimal():
    res = int(some_text)

elif some_text.count("-") <= 1:
    if some_text.replace("-", "").isdecimal():
        res = abs(int(some_text))

if some_text.count(".") == 1 and some_text.replace('.', '') \
        .replace('-', '').isdecimal():
    res = float(some_text)

if any(letter.isupper() for letter in some_text):
    res = some_text.lower()

else:
    res = some_text.upper()
print(res, type(res), sep="\n")
