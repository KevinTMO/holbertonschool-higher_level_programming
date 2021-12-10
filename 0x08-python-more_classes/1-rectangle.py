#!/usr/bin/python3
"""
Module 1-rectangle.py

Create prv inst attr width/height with their proper getter/setter

Class:
- Rectangle:

Methods:
- __init__()
- def width(self) / def width(self, value)
- def height(self) / def height(self, value)

Decorators:
- @property
- @setter
"""


class Rectangle:
    """
    Will get the width/height of a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initiate objects with attrs width/height
        Assign each attr with a value
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter of width attr to return the value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of width attr will set width with a value
        Validate if width is int or is greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter of heigth attr to return the value
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """
        Setter of height attr will set height with a value
        Validate if height is int or is greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__heigth = value
