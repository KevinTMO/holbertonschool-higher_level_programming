#!/usr/bin/python3
# Return a set of common elements


def common_elements(set_1, set_2):
    """
    set_1: first set of items
    set_2: second set of items
    """
    if set_1 is not None and set_2 is not None:
        return set_1 & set_2

    else:
        return None
