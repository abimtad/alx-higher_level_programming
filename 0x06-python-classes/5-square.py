#!/usr/bin/python3
"""Define a square with 'size'."""


class Square:
    """Represent a square with size 'size'."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The new square size.
        """
        self.size = size

    @property
    def size(self):
        """retrieve current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return are of the current square."""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for colm in range(self.__size):
                    print('#', end="")
                print("")
