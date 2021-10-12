#!/usr/bin/python3
"""
Module 2-is_same_class

Methods:
- def is_same_class(obj, a_class)
  - return true if the object (obj) is an instance of (a_class)
  - otherwise will return false
"""


def is_same_class(obj, a_class):
    """
    Return true if obj is type a_class
    Otherwise false
    """
    return type(obj) == a_class
