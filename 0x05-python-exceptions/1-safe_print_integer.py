#!/usr/bin/python3


def safe_print_integer(value):
    """
    This method should print an integer
    Using "{:d}".format()
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError:
        return False
