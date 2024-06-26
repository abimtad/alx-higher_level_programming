#!/usr/bin/python3

"""Define a square with size."""


class Square:
    """Represent a square with size 'size'."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retie the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                any(item < 0 for item in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        for blank_line in range(0, self.__position[1]):
            print("")
        for row in range(0, self.__size):
            for spc in range(0, self.__position[0]):
                print(" ", end="")
            for colm in range(0, self.__size):
                print("#", end="")
            print("")
