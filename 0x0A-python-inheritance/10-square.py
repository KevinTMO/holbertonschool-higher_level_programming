#!/usr/bin/python3
"""
Module: 10-rectangle

Method:
- def __init__(self, width, height)
  - Instantiation with super() to inherit from:
  ... base_geometry class.

Everything else will be called from inherited class Rectangle
Instatiation will be too on Rectangle class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Inherit from BaseGeometry methods
    """
    def __init__(self, size):
        """
        Using super() to call a method from BaseGeometry to validate
        Instantiation of width && height
        Size: private
        """
        self.integer_validator("size", size)  # send string name and validate
        super().__init__(size, size)  # instatiation of size using SC Rectangle
        self.__size = size  # giving result
