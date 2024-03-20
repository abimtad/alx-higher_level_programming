#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list."""
    a = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in a:
            a.append(my_list[i])
            result += my_list[i]
    return result
