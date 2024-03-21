#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    The function multiplies all the values of the dictionary by two.

    :param a_dictionary: A dictionary whose values are all integers.

    :return: A dictionary whose values all are multiplied by two.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
