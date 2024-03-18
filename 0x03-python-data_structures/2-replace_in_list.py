#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    The function replace an element at the specified index with another element

    :param my_list: The list that gets manipulated.
    :param idx: The index.
    :param element: The element to replace for.

    :return: The original list or the manipulated list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if idx == i:
            my_list[i] = element

    return my_list
