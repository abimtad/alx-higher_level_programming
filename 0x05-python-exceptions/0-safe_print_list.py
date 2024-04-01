#!/usr/bin/pyhton3

def safe_print_list(my_list=[], x=0):
    """
    The function print a specific number of element form the -
    list without space followed a newline.

    :param my_list: The list to print the items from.
    :param x: The number of items to print to the stdout.

    :return: The actual number of items printed to the stdout.
    """
    try:
        printed_elements = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_elements
