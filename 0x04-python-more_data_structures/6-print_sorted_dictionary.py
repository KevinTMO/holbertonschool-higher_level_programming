#!/usr/bin/python3
# Print a dictionary in alphabetic order


def print_sorted_dictionary(a_dictionary):
    """
    a_dictionary: a dictionary with key & values items
    """
    for key, value in sorted(a_dictionary.items()):
        print("{:s}: {}".format(key, value))
