# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def int_inicode(text: str) -> dict:
    res_dict = {}
    num1, num2 = map(int, text.split())
    res_dict.update({ord(num1): num1}, {ord(num2): num2})
    return sorted(res_dict.items(), key=lambda x: x[1])


print(int_inicode("15 12"))