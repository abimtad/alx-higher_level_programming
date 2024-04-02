#!/usr/bin/python3
"""Define a square with size."""


class Square:
    """Represent a square with size 'size'."""


    def __init__(self, size=0):
        """intialize a square.

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
