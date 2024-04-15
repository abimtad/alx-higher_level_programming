#!/usr/bin/python3
"""Defines a subclass of int."""


class MyInt(int):
    """Inverts equality operators."""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
