# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    correct = True
    for item in matrix:
        if len(item) != n:
            correct = False

    if correct:
        transposed_matrix = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            for j in range(n):
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix
    else:
        print("Не верная размерность матрицы")
        return


def print_matrix(matrix: list):
    for val in matrix:
        print(val)


matrix = [[1, 2, 4, 5], [1, 3, 5, 6], [3, 4, 5, 5], [1, 8, 2, 2]]
print_matrix(transpose(matrix))
