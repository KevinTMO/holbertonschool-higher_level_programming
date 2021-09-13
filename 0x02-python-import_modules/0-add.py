#!/usr/bin/python3
# Creating a function that call another function for addition

from add_0 import add

a = 1
b = 2

print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="")
print()
