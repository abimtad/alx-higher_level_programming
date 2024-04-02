#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    The function prints 'x' number of integer elements from a list.

    :param my_list: The list to print the integers form.
    :param x: The number of integers to print from the list.

    :return: The actual number of integers printed to the stdout.
    """
    count = 0  # Counter for the number of integers printed

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except IndexError:
        raise

    return count
