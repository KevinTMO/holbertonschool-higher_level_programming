#!/usr/bin/python3
# Print list of integers in reverse order


def print_reversed_list_integer(my_list=[]):
    """
    Will print a list of integers in reverse order
    my_list: is the list of integers
    """
    newList = my_list
    newList.reverse()

    for lst in newList:
        print("{:d}".format(lst))
