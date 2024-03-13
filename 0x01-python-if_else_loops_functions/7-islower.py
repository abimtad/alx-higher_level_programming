#!/usr/bin/python3
def islower(c):
    """Checks whether a character c is lower and returns a boolean value"""
    if ord(c) in range(97, 123):
        return True
    else:
        return False
