#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    The function add the first two integers of two tuples into a new tuple, if on of
    the tuple's size is less than 2 the vacant space is filled with 0.

    :param tuple_a: The first tuple.
    :param tuple_b: The second tuple.

    :return: The new tuple which is the addition of the first two integers of the tuples given.
    """
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    return (a[0] + b[0], a[1] + b[1])
