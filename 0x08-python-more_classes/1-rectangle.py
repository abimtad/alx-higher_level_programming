#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int):  Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise typeerror("width must be an integer")
        if value < 0:
            raise valueerror("width must be >= 0")
        self.__width = value

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def height(self):
        """Gets/sets the height of the rectangle."""
        return self.__height
