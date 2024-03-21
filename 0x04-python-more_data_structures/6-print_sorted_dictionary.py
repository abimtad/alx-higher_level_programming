#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    The function prints the key-value pairs of a dictionary; each on a new line,
    with alphabetic order of keys.

    :param a_dictionary: A dictionary.

    :return: None.
    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{0:s}: {1:}".format(key, a_dictionary[key]))
