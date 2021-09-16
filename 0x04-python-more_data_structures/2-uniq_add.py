#!/usr/bin/python3
# Sum all integers (Don't repeat)


def uniq_add(my_list=[]):
    """
    my_list: a list of integers
    """
    newList = my_list.copy()

    if len(newList) <= 0 or newList == None:
        return None

    return sum(set(newList))
