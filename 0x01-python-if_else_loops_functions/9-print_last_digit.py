#!/usr/bin/python3


def print_last_digit(number):
    """print the last digit of a number"""
    last_digit = abs(number) % 10
    print('{}'.format(last_digit), end="")
    return last_digit
