#!/usr/bin/python3
"""
Module 0-lookup

Includes a method called loopup that return an object
"""


def lookup(obj):
    """
    Return a list of attrs of an object
    """
    return dir(obj)
