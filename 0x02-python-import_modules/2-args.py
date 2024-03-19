#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{:d} argument{:s}:".format(num_arguments, 's' if num_arguments > 1 else ''))
        for idx, arg in enumerate(arguments, 1):
            print("{:d}: {:s}".format(idx, arg))
