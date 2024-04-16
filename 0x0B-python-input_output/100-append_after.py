#!/usr/bin/python3
"""Define text appender function."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line to a file, after each line containing a specific string."""
    with open(filename, 'r+', encode='utf-8') as f:
        for line in f.readlines():
            if search_string in line:
                f.write(new_string)
