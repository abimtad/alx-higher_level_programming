#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    The function computes the maximum integer from the list given and returns it back.

    :param my_list: The list, the max int is found from.

    :return: The max int from the list.
    """

    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for num in my_list:
            if num > max_int:
                max_int = num

    return max_int
