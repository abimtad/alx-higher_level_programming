#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arguments = argv
    Sum = 0
    for idx in range(1, len(arguments)):
        Sum += int(arguments[idx])

    else:
        print('{:d}'.format(Sum)
