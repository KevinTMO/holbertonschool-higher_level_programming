#!/usr/bin/python3
"""
Module 4-inherits_from.py

Methods:
- def inhertis_from(obj, a_class)
  - return true if the object (obj) is an instance of a class
  ... that inherited (directly of indirectly) from specefied class
  - otherwise will return false
"""


def inherits_from(obj, a_class):
    """
    Return true if obj is a sub class from a_class
    Otherwise false
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
