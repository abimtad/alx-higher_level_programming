#!/usr/bin/python3
"""Define a file appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to append.
        text (str): The text to append to the file.

    Return:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
