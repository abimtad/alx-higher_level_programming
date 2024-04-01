#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element 2 lists.

    Args:
        my_list_1 (list): dividend list
        my_list_2 (list): divider list
        list_length (int): the number of elements to be divide

    Returns:
        new list (length = list_length) with all divisions
    """

    result_list = []
    result = 1
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
   
