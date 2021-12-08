#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cpyDict = a_dictionary.copy()
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del cpyDict[key]

    return cpyDict
