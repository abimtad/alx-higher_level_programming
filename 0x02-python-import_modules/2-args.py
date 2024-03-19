#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} arguments:")
        for idx, arg in enumerate(arguments, 1):
            print(f"{idx}: {arg}")
