#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        plural_suffix = 's' if num_arguments != 1 else ''
        print(str(num_arguments) + " argument" + plural_suffix + ":")
        for idx, arg in enumerate(arguments, 1):
            print("{:d}: {:s}".format(idx, arg))
