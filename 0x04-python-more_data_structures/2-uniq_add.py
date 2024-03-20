#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in b list."""
    b = []
    resultt = 0
    for i in range(len(my_list)):
        if my_list[i] not in b:
            b.append(my_list[i])
            resultt += my_list[i]
    return resultt
