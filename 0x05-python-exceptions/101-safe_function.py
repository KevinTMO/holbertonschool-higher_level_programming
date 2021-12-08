#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        # result = fct(*args)
        # return result
        return fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as ve:
        stderr.write("Exception: {}\n".format(ve))
        return None
