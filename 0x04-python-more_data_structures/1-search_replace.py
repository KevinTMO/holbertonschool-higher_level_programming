#!/usr/bin/python3
# Replace all ocurrences with a new number


def search_replace(my_list, search, replace):
    """
    my_list: a list with integers
    search: the element to replace
    replace: the new element
    """
    newList = my_list.copy()

    for idx, value in enumerate(newList):
        if value == search:
            newList[idx] = replace
    return newList
