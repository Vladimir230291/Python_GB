# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
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


def storage():
    puzzle_dict = {
        "Загадка1": ["верный ответ", "да", "дальше"],
        "Загадка2": ["верный ответ", "да", "дальше"],
        "Загадка3": ["верный ответ", "да", "дальше"],
        "Загадка4": ["верный ответ", "да", "дальше"],
        "Загадка5": ["верный ответ", "да", "дальше"]
    }
    for puzz, ans in puzzle_dict.items():
        result = puzzle(puzz, ans)
        print(f"Потребовалось попыток: {result}")


if __name__ == "__main__":
    storage()
