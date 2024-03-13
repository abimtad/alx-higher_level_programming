#!/usr/bin/python3
def is_lower(c):
    """Checks whether a character c is lower and returns a boolean value"""
    for char in range(97, 123):
        if ord(c) == char:
            return True
    return False
