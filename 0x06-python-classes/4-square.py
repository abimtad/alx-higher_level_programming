#!/usr/bin/python3i
"""Defines a square with 'size'."""


class Square:
    """Represents a square with size 'size'."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """retrives current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the an appropriate valut to the variable 'size'"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the current square."""
        return (self.__size * self.__size)
