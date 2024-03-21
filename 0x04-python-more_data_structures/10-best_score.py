#!/usr/bin/python3
def best_score(a_dictionary):
    """
    The function finds the key with the highest integer value.

    :param a_dictionary: A dictionary whose key is a string literal -
    and whose value is always an integer.

    :return: The key with the highest value(integer)
    """
    if a_dictionary is None or not a_dictionary:
        return None
    best_key = None
    max_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
