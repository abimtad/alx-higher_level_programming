#!/usr/bin/python3
for tenth_dgt in range(10):
    for once_dgt in range(tenth_dgt + 1, 10):
        if once_dgt != 1:
            print(", ", end='')
        print("{0:d}{1:d}".format(tenth_dgt, once_dgt), end='')
else:
    print()
