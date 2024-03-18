#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    The function replace every number in the list with a boolean value
     based whether its is divisible by 2 or not.

    :param my_list: The list subject for the operation.

    :return: a new list where the numbers are replaced by boolean values.
    """

    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
