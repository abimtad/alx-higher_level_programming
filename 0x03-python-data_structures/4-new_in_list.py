#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    The function replaces an element at the specified index with another element and returns the copy of the list
    without manipulating the original list.

    :param my_list: The list.
    :param idx: The index.
    :param element: The element to replace for.

    :return: The copy of the  original list or a new manipulated list.
    """
    my_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if idx == i:
            my_list[i] = element

    return my_list
