#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    The function prints the key-value paris of a dictionary each on a new line,
    with alphabetic order of keys.

    :param a_dictionary: A dictionary.

    :return: None.
    
    :description: The function avoids printing a newline at the end -
    of the last output.
    """
    sorted_keys = sorted(a_dictionary.keys())
    for idx, key in enumerate(sorted_keys):
        if idx:
            print()
        print("{0:s}: {1:}".format(key, a_dictionary[key]), end='')
