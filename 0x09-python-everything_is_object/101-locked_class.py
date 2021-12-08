#!/usr/bin/python3
"""
Module: 101-locked_class.py

Prevents the user from dynamically creating a new instance attr
Except when calling "first_name"
"""


class LockedClass():
    """
    Defining a list with all attrs you want to use
    Anything not in the list cannot be used as attrs
    """
    __slot__ = "first_name"
