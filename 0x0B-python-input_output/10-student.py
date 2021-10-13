#!/usr/bin/python3
"""
Module: 9-student

Methods:
- def __init__(self, first_name, last_name, age):
  - instantiation of first_name, last_name, age
- def to_json(self, attrs=None):
  - retrieve a dictionary repr of a Student (class) instance
  ... if attrs is a list of strings then retrieve only those attrs names
  ... if not then retrieve all
"""


class Student:
    """
    Will instantiate and return a repr of a dictionary
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return a reprs of a dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            newDict = {}
            for lstAttrs in attrs:
                if lstAttrs in self.__dict__.keys():
                    newDict[lstAttrs] = self.__dict__[lstAttrs]
            return newDict
