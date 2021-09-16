#!/usr/bin/python3
# Return a set of all elements


def only_diff_elements(set_1, set_2):
    """
    set_1: first set of elements
    set_2: second set of elements
    """
    if len(set_1) != 0 or set_2 != 0:
        return set_1 ^ set_2

    else:
        return
