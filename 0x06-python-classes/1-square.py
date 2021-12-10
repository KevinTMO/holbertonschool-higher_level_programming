#!/usr/bin/python3
"""
Module: 1-square.py

Define the square class adding a private instance attr

Class:
- Square():

Instance attr:
- size (private)

"""


class Square:
    """
    Method:
    - __init__()
    """
    def __init__(self, size):
        """
        Instance attrs:
        - size (private)
        """
        self.__size = size
