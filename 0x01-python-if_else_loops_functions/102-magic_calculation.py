#!/usr/bin/python3


def magic_calculation(a, b, c):
    """magic calculator"""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a*b - c)
