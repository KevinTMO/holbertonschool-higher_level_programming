#!/usr/bin/python3
# Delete a key in a dictionary


def simple_delete(a_dictionary, key=""):
    """
    a_dictionary: contains the key, value items
    key: is the first item of the dictionary
    """
    if a_dictionary is None:
        return None

    a_dictionary.pop(key, None)
    return a_dictionary
