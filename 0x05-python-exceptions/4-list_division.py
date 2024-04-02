#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    The function divided one element of a list by other and forms a list of -
    quotients. If there is a problem when -
    dividing, the list will be filled by zeros while logging the error -
    occurred to the stdout.

    :param my_list_1: Lists which are dividends.
    :param my_list_2: Lists which are divisors.
    :param list_length: The number of elements to divide starting -
    from the index 0(first element).

    :return: A list of quotients, or an empty list if both empty -
    lists are provided.
    """
    result = []

    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
            result.append(quotient)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        finally:
            pass
    return result