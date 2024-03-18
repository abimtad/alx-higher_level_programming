#!/usr/bin/python3
def no_c(my_string):
    """
    The function remove every occurrence of the letters 'c' & 'C' form the string.

    :param my_string: The string to be manipulated.

    :return: Manipulated string.
    """
    new_string = ""
    for sub_string in my_string:
        if sub_string != 'c' and sub_string != 'C':
            new_string += sub_string

    return new_string
