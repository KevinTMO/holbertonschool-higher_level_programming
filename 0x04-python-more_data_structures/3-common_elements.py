#!/usr/bin/python3
# Return a set of common elements


def common_elements(set_1, set_2):
    """
    set_1: first set of items
    set_2: second set of items
    """
    if set_1 and set_2:
        return set_1 & set_2

    else:
        return
