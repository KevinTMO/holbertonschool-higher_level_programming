#!/usr/bin/python3
# Print the last digit of a number


def print_last_digit(number):
    number = abs(number) % 10
    print("{:d}".format(number), end='')
    return (number)
