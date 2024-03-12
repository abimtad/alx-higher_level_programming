#!/usr/bin/python3


def islower(c):
    """check if c is lower case"""
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
