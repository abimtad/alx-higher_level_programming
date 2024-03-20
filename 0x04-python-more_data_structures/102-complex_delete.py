#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    while value in a_dictionary.values():
        for a, b in a_dictionary.items():
            if b == value:
                del a_dictionary[a]
                break
    return a_dictionary
