#!/usr/bin/python3


def print_square(size):
    """
    This method should print a square
    Size: is the length of the square
    - size must be an integer
         - otherwise rise TypeError
    - if size is less than 0:
         - raise ValueError
    - if size is float and less than 0:
         - raise TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
