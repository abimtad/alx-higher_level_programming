# !/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    The function searches for an element in a list and replaces every
    occurrence of the element with another.

    :param my_list: The matrix to search for an element.
    :param search: The element to search for.
    :param replace: The element to replace with.

    :return: A new list with the targeted element replaced.
    """
    replaced_list = [replace if x == search in my_list else x for x in my_list]

    return replaced_list
