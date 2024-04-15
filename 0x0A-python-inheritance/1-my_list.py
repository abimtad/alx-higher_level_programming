#!/usr/bin/python3
"""Define a class that inherits form class list."""

class MyList(list):
    """implements sorted printinig."""

    def print_sorted(self):
        """sortes the list."""
        print(sorted(self))
