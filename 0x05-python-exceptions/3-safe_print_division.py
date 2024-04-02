#!/usr/bin/python3

def safe_print_division(a, b):
    """
    The function computes quotient of two numbers and prints it.

    :param a: The dividend.
    :param b: The divisor.

    :return: The quotient or None, if the type or value of the -
    operands is not appropriate.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {0}".format(result))
        return result
