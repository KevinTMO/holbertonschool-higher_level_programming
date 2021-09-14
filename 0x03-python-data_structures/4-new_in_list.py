#!/usr/bin/python3
# Copy a list


def new_in_list(my_list, idx, element):
    """
    Will copy a list to an empty list
    my_list: is the one we need to copy
    idx: is the pos to replace
    element: is the element we use to replace another
    """

    newList = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return newList

    else:
        newList[idx] = element
        return newList
