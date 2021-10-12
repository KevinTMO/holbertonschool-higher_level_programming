#!/usr/bin/python3
"""
Module: 8-rectangle

Method:
- def __init__(self, width, height)
  - Instantiation with super() to inherit from:
  ... base_geometry class.
- def area(self, width, height):
  - Calculate the area of a rectangle using the formula:
  ... width * height
  - print() will print and str() will return but both should do:
  ... "[Rectangle] <width>/<height>"
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherit from BaseGeometry methods
    """
    def __init__(self, width, height):
        """
        Using super() to call a method from BaseGeometry to validate
        Instantiation of width && height
        width: private
        height: private
        """
        super().integer_validator("width", width)  # send width name and val
        self.__width = width  # giving result
        super().integer_validator("height", height)  # send height name and val
        self.__height = height  # giving result

    def area(self):
        """
        Calculate the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string that represents the object
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__width,
                                         self.__height)
