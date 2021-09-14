#!/usr/bin/python3
# Print a list of integers


def print_list_integer(my_list=[]):
    """
    Will print a list of integers
    my_list: is the list of integers to print
    """
    for lst in my_list:
        print("{:d}".format(lst))
