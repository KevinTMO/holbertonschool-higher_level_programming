#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if len(a_dictionary) == 0:
        return None

    if a_dictionary:
        for key in list(a_dictionary.keys()):
            if a_dictionary[key] == value:
                del a_dictionary[key]

        return a_dictionary
