#!/usr/bin/python3
"""
Module: 6-base_geometry

Methods:
- def area(self)
  - Raise an Exception with a message area() is not implemented
- def integer_validator(self, name, value)
  - will validate value to be:
    - Integer
    - Greater than 0
  - Raise exception if value is one of these:
    - Value is not INT
    - Value is less or equal to 0
"""


class BaseGeometry:
    """
    Include Two Methods
    """
    def area(self):
        """
        Will raise an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value to be INT and greater than 0 else:
        Exceptions:
           - TypeError
             - Message "<name> must be an integer"
           - ValueError
             - Message "<name> must be greater than 0"
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
