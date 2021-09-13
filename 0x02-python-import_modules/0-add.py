#!/usr/bin/python3
# Creating a function that call another function for addition

if __name__ == "__main__":

    from add_0 import add

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
