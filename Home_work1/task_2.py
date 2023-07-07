# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
LOWER_LIMIT = 1
UPPER_LIMIT = 100_000
number = int(input(f"Введите число положительное, не больше {UPPER_LIMIT}: "))
if LOWER_LIMIT <= number <= UPPER_LIMIT:
    if number == 1:
        print("Число составное")
        exit()
    for i in range(2,number):
        if number % i == 0:
            print("Число составное")
            exit()
    print("Число простое")
else:
    print("Введите корректное значение!")