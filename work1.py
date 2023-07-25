
import numpy as np

class Matrix:

    def __init__(self, matr1,matr2):
        self.matr1 = np.array(matr1)
        self.matr2 = np.array(matr2)


    def finding_matrix(self):
        print(self.matr1)
        print(self.matr2)


    def comparison_matrix(self):
        return np.array_equal(self.matr1,self.matr2)

    def multiplication_matrix(self):
        return np.dot(self.matr1, self.matr2)

    def additions_matrix(self):
        return self.matr1 + self.matr2

A = [[1, -2], [2, 3]]
B = [[4, 5], [6, 7]]

m = Matrix(A, B)

print(f'Вывод матриц А и В на экран {m.finding_matrix()}')
print(f'Сравнение матриц А и В __->__{m.comparison_matrix()}')
print(f'Умножение матриц А и В __->__{m.multiplication_matrix()}')
print(f'Сложение матриц А и В __->__{m.additions_matrix()}')


