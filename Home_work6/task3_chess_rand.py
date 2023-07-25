# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

# from sem6_import_module.chess import random_coordinates, get_queen_coordinates, queens_attack
from sem6_import_module import chess


if __name__ == "__main__":

    SUCCES_PLACEMENT = 4
    count = 0
    placement = []
    while count != SUCCES_PLACEMENT:

        queens = chess.random_coordinates()
        if chess.queens_attack(queens):
            placement.append(queens)
            count += 1
            print(count)
        else:
            queens.clear()

    print(placement)
