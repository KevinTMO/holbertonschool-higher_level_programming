#!/usr/bin/python3
# Get the max value of a dictionary


def best_score(a_dictionary):
    """
    a_dictionary: contains the key, value items
    """
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
