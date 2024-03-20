#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    anew_dictionary = {}
    for a, b in a_dictionary.items():
        anew_dictionary[a] = b * 2
    return anew_dictionary
