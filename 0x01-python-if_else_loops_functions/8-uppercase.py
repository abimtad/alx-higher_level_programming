#!/usr/bin/python3
def uppercase(string):
    """Changes a string str to uppercased string"""
    for char in string:
        char_code = ord(char)
        if char_code in range(97, 123):
            char_code -= 32
        print('{0:s}'.format(chr(char_code)), end='')
    else:
        print()
