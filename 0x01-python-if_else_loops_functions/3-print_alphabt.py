#!/usr/bin/python3
for char_code in range(97, 123):
    if chr(char_code) != 'e' and chr(char_code) != 'q':
        print('{0}'.format(chr(char_code)), end='')
