#!/usr/bin/python3
# Multiply every value of the dictionary by 2


def multiply_by_2(a_dictionary):
    """
    a_dictionary: contains the key, value items
    """
    newDict = {}

    for key, value in a_dictionary.items():
        newValue = value * 2
        newDict.update({key: newValue})
    return newDict
