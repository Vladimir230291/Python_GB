# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.
def dec_to_hex(num:int) -> str:
    hex_char = "0123456789ABCDEF"
    hex_str = ""

    if num == 0:
        return "0"

    elif num < 0:
        num = abs(num)
        hex_str += "-"

    while num > 0:
        remainder_division = num % 16
        hex_str = hex_char[remainder_division] + hex_str
        num = num // 16

    return hex_str


num = int(input("Введите целое число: "))
hex_str = dec_to_hex(num)
print(f"Шестнадцатеричное представление: {hex_str}")
print(f"Представление через втроенную фукцию: {hex(num)}")
