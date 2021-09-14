#!/usr/bin/python3
# Sum two different tuples


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Sum two tuples
    tuple_a: a tuple with integers
    tuple_b: a tuple with integers
    """

    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
