#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    The function removes a list at the specified index.

    :param my_list: The list to remove the element from.
    :param idx: The position to remove the element.

    :return: a list whose element at index is removed or the original list.
    """
    if idx < 0 and idx >= len(my_list):
        return my_list

    for element_idx in range(len(my_list)):
        if element_idx == idx:
            del my_list[idx]

    return my_list
