#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces all occurrences of
    an element by another in a new list"""

    anew_list = my_list[:]
    for j in range(len(anew_list)):
        if anew_list[j] == search:
            anew_list[j] = replace

    return (anew_list)
