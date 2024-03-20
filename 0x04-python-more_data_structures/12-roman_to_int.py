#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    conv_int = 0
    tmp_int = 0
    for i in reversed(roman_string):
        if roman_int[i] < tmp_int:
            conv_int -= roman_int[i]
        else:
            conv_int += roman_int[i]
        tmp_int = roman_int[i]
    return conv_int
