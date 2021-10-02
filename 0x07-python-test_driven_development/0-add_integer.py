#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Check if a && b are same type as int
    if not then raise error TypeError
    If true then return a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer")
    else:
        return int(a) + int(b)
