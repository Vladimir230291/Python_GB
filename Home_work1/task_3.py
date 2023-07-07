# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 100
COUNT_LIMIT = 10

num = randint(LOWER_LIMIT,UPPER_LIMIT)
count = 0
seach_input = None

print(f"Угадайте, загаданное число, от {LOWER_LIMIT} до {UPPER_LIMIT}, за {COUNT_LIMIT} попыток")

while count < COUNT_LIMIT:
    count += 1
    seach_input = int(input("Введите число: "))

    if seach_input < num:
        print("Загаданное число больше")
    elif seach_input > num:
        print("Загаданное число меньше")
    else:
        print(f"Вы угадали число!!! количество попыток: {count}")
else:
    print(f"Попытки кончились, загаданное число: {num}")