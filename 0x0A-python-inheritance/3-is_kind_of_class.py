#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Methods:
- def is_kind_of_class(obj, a_class)
  - return true if the object (obj) is an instance of (a_class) or
  ... if the object (obj) is an instance of a class that inherited from
  - otherwise will return false
"""


def is_kind_of_class(obj, a_class):
    """
    Return true if obj is type a_class
    Otherwise false
    """
    return isinstance(obj, a_class)
