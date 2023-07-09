# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import fractions

print("Шаблон записи дроби: ( a/b ) через '/'\n")


def calculate_fraction(num1, denum1, num2, denum2):
    # Вычисление суммы дробей
    sum_numerator = num1 * denum2 + num2 * denum1
    sum_denomerator = denum1 * denum2

    # Вычисление произведения дробей
    product_num = num1 * num2
    product_denom = denum1 * denum2

    # Нахождение наибольшего общего делителя для суммы и произведения дробей
    gcd_sum = nod(sum_numerator, sum_denomerator)
    gcd_product = nod(product_num, product_denom)

    # Упрощение дробей
    sum_numerator //= gcd_sum
    sum_denomerator //= gcd_sum
    product_num //= gcd_product
    product_denom //= gcd_product

    return f'Сумма дробей: {sum_numerator}/{sum_denomerator}, Произведение дробей: {product_num}/{product_denom}\n'


# Метод для нахождения наибольший общий делитель
def nod(a, b):
    while b:
        a, b = b, a % b
    return a


numerator1, denumerator1 = map(int, input("Введите первую дробь: ").split("/"))
numerator2, denumerator2 = map(int, input("Введите вторую дробь: ").split("/"))

result = calculate_fraction(numerator1, denumerator1, numerator2, denumerator2)
print(result)
# Проверка
print(f"fractions(+): {fractions.Fraction(numerator1, denumerator1) + fractions.Fraction(numerator2, denumerator2)}")
print(f"fractions(*): {fractions.Fraction(numerator1, denumerator1) * fractions.Fraction(numerator2, denumerator2)}")
