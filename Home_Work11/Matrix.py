# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    """
    Class for created matrix
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        """
        Method for print matrix
        """
        matrix_str = ""
        for row in self.matrix:
            print(row)
        return matrix_str

    def __eq__(self, other):
        """
        Метод для корректного сравнения матриц
        :param other: list
        :return: bool
        """
        return self.matrix == other.matrix

    def __add__(self, other):
        """
        Метод сложения матриц
        """
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError("Матрицы должны иметь одинаковый размер.")

    def __mul__(self, other):
        """
        Умножение матриц
        """
        if len(self.matrix[0]) == len(other.matrix):
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    elem = 0
                    for k in range(len(other.matrix)):
                        elem += self.matrix[i][k] * other.matrix[k][j]
                    row.append(elem)
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError(
                "Количество столбцов в 1-ой матрице должно быть равно количеству строк во 2-ой матрице.")


if __name__ == "__main__":
    matr1 = Matrix([[13, 12, 53], [4, 35, 61], [7, 28, 93]])
    matr2 = Matrix([[31, 23, 33], [4, 51, 61], [7, 82, 93]])
    print(matr1)
    print(matr2)
    print(f"Сравнение на равернство: {matr1 == matr2}\n")
    print("Результат умножения матриц:")
    print(matr1 * matr2)
    print("Результат сложения матриц:")
    print(matr1 + matr2)

