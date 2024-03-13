#!/usr/bin/python3
for numbr in range(0, 100):
    if numbr < 99:
        print('{}{}'.format(numbr // 10, numbr % 10), end=", ")
    elif numbr == 99:
        print(numbr)
