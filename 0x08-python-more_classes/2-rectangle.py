#!/usr/bin/python3
"""
Module 2-rectangle.py

Create area/perimeter methods

Class:
- Rectangle:

Methods:
- __init__()
- def width(self) / def width(self, value)
- def height(self) / def height(self, value)
- def area(self)
- def perimeter(self)
   - if width or height == 0 then perimeter is == 0

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
        return self.__height

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
            self.__height = value

    def area(self):
        """
        Return the area of a rectangle using height + width
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of a rectangle using heigth + width
        if height or width are == 0 then perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return 2 * (self.__width + self.__height)
