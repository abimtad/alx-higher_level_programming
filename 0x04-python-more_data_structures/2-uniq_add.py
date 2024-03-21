#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    The function adds every one occurrence of a list of integers.

    :param my_list: The list of integers.

    :return: A single integer which is a unique sum of the list.
    """
    Sum = 0

    for uniq_num in set(my_list):
        Sum += uniq_num

    return Sum
