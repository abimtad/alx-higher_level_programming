#!/usr/bin/python3
"""Define class or inhertance checker."""

def is_kind_of_class(obj, a_class):
    """check if object is an instance of,
    or instance of a class that inherited from

    Args:
        obj (any): the object to be checked
        a_class (type): the class to be matched
    Return:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    return False
