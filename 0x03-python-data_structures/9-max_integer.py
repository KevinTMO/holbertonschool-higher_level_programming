#!/usr/bin/python3
# Return the biggest integer in the list


def max_integer(my_list=[]):
    """
    Will return the biggest integer in the list
    my_list: is the list with integers
    """
    if my_list:
        maxInt = 0

        for numbers in my_list:
            if numbers > maxInt:
                maxInt = numbers
        return maxInt
