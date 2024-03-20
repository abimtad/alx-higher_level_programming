#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for j in matrix:
        square_matrix.append(list(map(lambda y: y**2, j)))
    return (squared_matrix)
