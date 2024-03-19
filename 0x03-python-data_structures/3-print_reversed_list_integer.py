#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    The function prints the integers in the provided list in a reversed
    order, each on a new line.

    :param my_list: The list

    :return: None
    """
    if isinstance(my_list, list):
        if not my_list:
            print()
        for i in range(len(my_list) - 1, -1, -1):
            print('{:d}'.format(my_list[i]))
