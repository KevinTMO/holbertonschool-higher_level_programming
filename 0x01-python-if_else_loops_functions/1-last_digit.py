#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    LastDigit = number % -10
else:
    LastDigit = number % 10
# print("Last digit of {:d} is {:d}".format(number, LastDigit), end='')
if LastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, LastDigit))
elif LastDigit is 0:
    print("Last digit of {:d} is {:d} and is zero"
          .format(number, LastDigit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, LastDigit))
