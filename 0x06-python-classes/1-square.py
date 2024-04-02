#!/usr/bin/python3
"""Defines a class square by size"""


class Square:
    """represent a squar of size 'size'. """

    def __init__(self, size):
        """Intailize a new square.

        Args:
            size (int): size of the square.
        """
        self.__size = size
