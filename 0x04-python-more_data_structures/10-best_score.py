#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""

    if a_dictionary:
        big_int = 0
        for key in a_dictionary.keys():
            if a_dictionary[key] > big_int:
                big_int = a_dictionary[key]
        idx = list(a_dictionary.values()).index(big_int)
        return list(a_dictionary.keys())[idx]
    else:
        return None
