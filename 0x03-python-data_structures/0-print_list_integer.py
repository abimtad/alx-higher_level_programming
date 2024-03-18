#! /usr/bin/python3
def print_list_integer(my_list=[]):
    """
    This function prints the integer values of a list, each in a new line.

    Parameters:
    my_list: The list containing the integer numbers.

    Return: None
    """

    for integer_idx in range(len(my_list)):
        print('{:d}'.format(my_list[integer_idx]))
