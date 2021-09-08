#!/usr/bin/python3


def fizzbuzz():
    for number in range(1, 100 + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ".format(number), end="")
        elif number % 3 == 0:
            print("Fizz ".format(number), end="")
        elif number % 5 == 0:
            print("Buzz ".format(number), end="")
        else:
            print("{:d} ".format(number), end="")
