#!/usr/bin/python3
# Replace an element in specific pos


def replace_in_list(my_list, idx, element):
    """
    Will replace an element at idx pos
    my_list: the list of integers
    idx: the pos to replace
    element: the element that will replace another element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
