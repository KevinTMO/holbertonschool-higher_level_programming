#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    This method will receive strings
    if they are not strings raise TypeError
    Message: first_name must be a string / Last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name), end="")
    print()
