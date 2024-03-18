#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function prints the integers given int the -
    matrix as a matrix of integers.

    :param matrix: The two-dimensional list to print.

    :return: None.
    """
    for row in matrix:
        for element in row:
            if row.index(element) != len(row) - 1:
                print('{:d}'.format(element), end=' ')
            else:
                print('{:d}'.format(element))
