#!/usr/bin/python3
# Sum all integers (Don't repeat)


def uniq_add(my_list=[]):
    """
    my_list: a list of integers
    """
    if my_list:
        newList = my_list.copy()

    return sum(set(newList))
