#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for item in matrix:
        new_matrix = map(item**2, item)
    return new_matrix
