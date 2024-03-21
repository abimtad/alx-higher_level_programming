#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    The function coverts a roman numeral into its arabic numeral counterpart.

    :param roman_string: A roman number, represents up to 3999.

    :return: Arabic counterpart of the roman numeral.
    """
    if not isinstance(roman_string, str) and roman_string is None:
        return 0

    roman_numeral = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }
    arabic_numeral = 0
    length = len(roman_string)
    for i in range(length):
        value = roman_numeral.get(roman_string[i])

        if i < length - 1 and value < roman_numeral.get(roman_string[i + 1]):
            arabic_numeral -= value
        else:
            arabic_numeral += value

    return arabic_numeral
