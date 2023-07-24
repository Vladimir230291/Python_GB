# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

"""
Загадка
"""
COUNT_TRY = 2

def puzzle(text_puzzle: str, answers: list[str], trials: int = COUNT_TRY):
    count = 0
    print(text_puzzle)
    while trials > 0:
        count += 1
        user_answer = input(f"Осталось попыток: {trials}, Ваш ответ: ")
        if user_answer.lower() in answers:
            return count
        trials -= 1
    else:
        return trials


if __name__ == "__main__":
    print(puzzle("Типо загадка", ["верный ответ", "да", "нет"]))
