#!/usr/bin/python3
"""Defines a class that inherits form class list."""

class MyList(list):
    """implements sorted printinig."""

    def print_sorted(self):
        """sorts the list."""
        print(sorted(self))
