#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv
    if len(arguments) == 1:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(arguments) - 1))
        for idx in range(1, len(arguments)):
            print("{:d}: {:s}".format(idx, arguments[idx]))
