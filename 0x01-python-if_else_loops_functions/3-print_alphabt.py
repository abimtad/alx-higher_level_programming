#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) != 'q' and chr(char) != 'e':
        print('{}'.format(chr(char)), end="")
