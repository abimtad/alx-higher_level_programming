#!/usr/bin/python3


def fizzbuzz():
    """prints the numbrbers from 1 to 100 separated by a space"""
    for numbr in range(1, 101):
        if numbr % 3 == 0 and numbr % 5 != 0:
            print('Fizz', end=" ")
        elif numbr % 5 == 0 and numbr % 3 != 0:
            print('Buzz', end=" ")
        elif numbr % 15 == 0:
            print('FizzBuzz', end=" ")
        else:
            print(numbr, end=" ")
