#!/usr/bin/python3
"""
Module: 8-rectangle

Method:
- def __init__(self, width, height)
  - Instantiation with super() to inherit from:
  ... base_geometry class.
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
