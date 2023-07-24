# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь

from random import randint

__all__ = ["get_queen_coordinates", "queens_attack", "random_coordinates"]

__LIMIT_QUEENS = 8
__HIGHT_LIMIT = 8
__LOW_LIMIT = 1


def queens_attack(queens) -> bool:
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):

            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def get_queen_coordinates() -> list:
    queens = []
    count = 0
    num_queen = 1
    while count < __LIMIT_QUEENS:
        x, y = map(int, input(f"Введите координаты ферзя {num_queen} от 1 до 8 (x, y): ").split())
        if __LOW_LIMIT <= x <= __HIGHT_LIMIT and __LOW_LIMIT <= y <= __HIGHT_LIMIT:
            num_queen += 1
            count += 1
            queens.append((x, y))
        else:
            print("не корректные координаты")
            continue
    return queens


def random_coordinates() -> list:
    queens = []
    count = 0
    while count < __LIMIT_QUEENS:
        x = randint(1, 8)
        y = randint(1, 8)
        if x != y:
            queens.append((x, y))
            count += 1
        else:
            continue
    return queens


if __name__ == "__main__":
    queens = get_queen_coordinates()
    print(queens_attack(queens))
