#!/usr/bin/python3
# Retrieves an element at idx pos


def element_at(my_list, idx):
    """
    Retrieves an element at idx pos
    my_list: is the list of integers
    idx: is the position of the element to print
    """
    if idx < 0 or idx >= len(my_list):
        return None

    else:
        return my_list[idx]
