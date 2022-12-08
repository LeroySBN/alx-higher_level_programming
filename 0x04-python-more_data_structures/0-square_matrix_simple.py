#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2

    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append(list(map(square, matrix[i])))
    return new_matrix
