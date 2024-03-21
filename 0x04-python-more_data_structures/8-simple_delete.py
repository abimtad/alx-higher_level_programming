#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    The function deletes an item from a dictionary with a provided key.

    :param a_dictionary: A dictionary.
    :param key: A key.

    :return: A dictionary whose item is deleted or intact dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
