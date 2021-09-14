#!/usr/bin/python3
# Remove multiple characters in a string


def no_c(my_string):
    """
    Remove multiple characters in a string
    my_string: the string to remove  characters from
    """
    newString = my_string
    chrRem = "Cc"

    for characters in chrRem:
        newString = newString.replace(characters, "")

    return newString
