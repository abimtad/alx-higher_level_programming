#!/usr/bin/python3


def raise_exception_msg(message=""):
    """raises a name exception with a message."""
    try:
        raise NameError
    except NameError:
        print(message)
