#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    The function updates a dictionary with the provided key and value pair.

    :param a_dictionary: The dictionary to update.
    :param key: Dict key.
    :param value: Dict value.

    :return: Updated dictionary.
    """
    if isinstance(a_dictionary, dict):
        a_dictionary[key] = value

    return a_dictionary
