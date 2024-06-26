#!/usr/bin/python3
"""Defines a function that reads a txt file."""


def read_file(filename=""):
    """prints the content of a file with encoding UTF-8."""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
