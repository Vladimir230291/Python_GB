# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint


def guessing_game():
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_ATTEMPTS = 1
    MAX_ATTEMPS = 10

    def check_guess():
        print("Угадайте число от", MIN_NUM, "до", MAX_NUM)
        secret_number = randint(MIN_NUM, MAX_NUM)
        num_attempts = int(input("Введите колличество попыток(1-10): "))

        while num_attempts:
            guess_num = int(input("Введите число: "))
            num_attempts -= 1

            if guess_num == secret_number:
                print(f"Поздравляю! Вы угадали число остаток попыток {num_attempts}")
                break
            elif guess_num < secret_number:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
        else:
            print("Загаданно было", secret_number)

    return check_guess


guessing_game()
