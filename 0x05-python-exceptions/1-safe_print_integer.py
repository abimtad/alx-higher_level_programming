#!/usr/bin/python3

def safe_print_integer(value):
    """
    The function prints only an integer value if sth else is provided -
    it won't print instead it returns False, True and prints the value -
    if integer is provided.

    :param value: The value to print.

    :return: True if integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
