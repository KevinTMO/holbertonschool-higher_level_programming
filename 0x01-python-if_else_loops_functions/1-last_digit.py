#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    LastDigit = number % -10
else:
    LastDigit = number % 10

print("Last digit of {:d} is {:d}".format(number, LastDigit), end='')

if LastDigit > 5:
    print(" and is greater than 5")
elif LastDigit is 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
