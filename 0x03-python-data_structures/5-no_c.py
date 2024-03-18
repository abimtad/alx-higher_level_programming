#!/usr/bin/python3
def no_c(my_string):
    """
    The function remove every occurrence of the letters 'c' & 'C' form the string.

    :param my_string: The string to be manipulated.

    :return: Manipulated string.
    """
    new_string = ""
    for char_idx in range(len(my_string)):
        if my_string[char_idx] != 'c' and my_string[char_idx] != 'C':
            new_string += my_string[char_idx]

    return new_string
