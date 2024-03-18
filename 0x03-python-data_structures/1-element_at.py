def element_at(my_list, idx):
    """
    The function returns the element at the specified index.

    :param my_list: The list
    :param idx: The index of the element intended to be extracted.

    :return: the element at the index or None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    for i in range(len(my_list)):
        if idx == i:
            return my_list[i]
