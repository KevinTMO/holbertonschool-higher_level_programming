#!/usr/bin/python3
"""
Module: 6-base_geometry

Methods: def area(self)
- Raise an Exception with a message area() is not implemented
"""


class BaseGeometry:
    """
    Include One Method to raise Exception message
    """
    def area(self):
        """
        Will raise an exception message
        """
        raise Exception("area() is not implemented")
