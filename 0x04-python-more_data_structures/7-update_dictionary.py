#!/usr/bin/python3
# Updated a dictionary creating or overwriting an existing value


def update_dictionary(a_dictionary, key, value):
    """
    a_dictionary: dictionary with key, value
    key: will be the first item of a pair
    value: the second item of a pair
    """

    newDict = {key: value}

    a_dictionary.update(newDict)

    return a_dictionary
