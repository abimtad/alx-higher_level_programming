#!/usr/bin/python3
"""Define a subclass of int."""

class MyInt(int):
    """Invertes equality operators."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value
    
    def __ne__(self, value):
        """Override != opeartor with == behavior."""
        return self.real == value
