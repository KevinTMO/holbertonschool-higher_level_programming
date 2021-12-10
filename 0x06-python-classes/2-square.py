#!/usr/bin/python3
"""
Module: 2-square.py

Validate the instance attr size if it is an integer

Class:
- Square():

Instance attr:
- size (private)

Validation:
- If size is an integer then assign the value
  - If not then just raise a TypeError or ValueError with a msg
"""


class Square:
    """
    Method:
    - __init__()
    """
    def __init__(self, size=0):
        """
        Instance attrs:
        - size (private)

        Validate that size is an integer or not
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
