#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print x int in a list.

    Args:
        my_list (list): The list to be iterated
        x (int): The number of elements

    Returns:
        elements printed
    """
    k = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            k += 1
        except (ValueError, TypeError):
            continue
    print("")
    return k
