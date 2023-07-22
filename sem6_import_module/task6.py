# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение

"""
Загадка
"""
__all__ = ["puzzle", "storage", "show_stat"]
COUNT_TRY = 2
_data = {}


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
    for _puzzle, ans in puzzle_dict.items():
        puzzle_result = puzzle(_puzzle, ans)
        add_log(_puzzle, puzzle_result)
        print(f"Потребовалось попыток: {puzzle_result}")


def add_log(puzzle_text: str, try_count: int):
    _data.update({puzzle_text: try_count})


def show_stat():
    print("Статистика:")
    res = "\n".join(f'Загадка {puzzle_text}. '
                    f'{f"Угадана с {trial_count} попытки." if trial_count > 0 else "не угадана"}'
                    for puzzle_text, trial_count in _data.items())
    print(res)


if __name__ == "__main__":
    storage()
    show_stat()
