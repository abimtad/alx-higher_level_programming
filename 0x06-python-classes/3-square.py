#!/usr/bin/python3
"""Defines a square with size 'size'."""


class Square:
    """represents a square with size 'size'."""

    def __init__(self, size=0):
        """initializes square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the current square."""
        return self.__size ** 2
