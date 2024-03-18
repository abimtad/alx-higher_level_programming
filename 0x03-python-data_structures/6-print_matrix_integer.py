#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    The function prints the integers given in the matrix as a matrix of integers.

    :param matrix: The two-dimensional list to print.

    :return: None.
    """
    for row in matrix:
        for i in range(len(row)):
            print('{:d}'.format(row[i]), end=' ')
        print()
