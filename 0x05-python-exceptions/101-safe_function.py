#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as ve:
        stderr.write("Exception: {}\n".format(ve))
        return None
