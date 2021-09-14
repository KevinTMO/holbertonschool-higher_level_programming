#!/usr/bin/python3
# Return the biggest integer in the list


def max_integer(my_list=[]):
    """
    Will return the biggest integer in the list
    my_list: is the list with integers
    """
    if len(my_list) == 0:
        return None

    else:
        maxInt = 0

        for number in my_list:
            if number > maxInt:
                maxInt = number
        return maxInt
