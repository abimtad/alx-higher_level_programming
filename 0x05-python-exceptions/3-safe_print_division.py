#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides 2 integers and prints the result.

    Args:
        a (int): dividend
        b (int): diviser

    Returns:
        value of the devision, Otherwise: None
    """

    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
