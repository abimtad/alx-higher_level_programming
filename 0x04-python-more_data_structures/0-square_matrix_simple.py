#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    The function squares every element of the matrix and returns a new matrix.

    :param matrix: The two-dimensional matrix.

    :return: A new squared matrix.
    """
    if isinstance(matrix, list):
        new_matrix = list(map(lambda _list: [x**2 for x in _list], matrix))

    return new_matrix
