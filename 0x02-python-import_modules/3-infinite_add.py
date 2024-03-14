#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the sum of all the arguments"""
    import sys

    result = 0
    for args in range(1, len(sys.argv)):
        result += int(sys.argv[args])
    print(result)
