#!/usr/bin/python3
"""
Module: 4-square.py

Print a square using # by size until range(size)

Class:
- Square():

Instance attr:
- size (private)

Methods:
- __init__()
- area()
- size(self) -> getter
- size(self, value) -> setter
  - Will validate now instead of __init__
- my_print(self)

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
        """
        self.__size = size

    def area(self):
        """
        Get the area of a square and return it
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter will return size after setter
        Getter use "property" decorator
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter will set the value for size before retrieve it
        Now will validate too if it is an int or greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Print a square using # by size until range(size)
        """
        if self.size == 0:
            pass
        print('\n'.join("#" * self.size for sq in range(self.size)))
