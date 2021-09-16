#!/usr/bin/python3
# Return a set of common elements


def common_elements(set_1, set_2):
    """
    set_1: first set of items
    set_2: second set of items
    """
    if len(set_1) != 0 or len(set_2) != 0:
        return set_1 & set_2

    else:
        return
