#!/usr/bin/python3
def multiple_returns(sentence):
    """
    The function takes a string then finds the length and -
    the first character afterward returns the length and first
    character as a tuple, one followed by another.

    :param sentence: The string, i.e. the data extracted from.

    :return: A tuple, containing the length and first character or length and
    None if the string is empty.
    """

    if len(sentence) == 0:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
