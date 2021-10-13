#!/usr/bin/python3
"""
Module: 9-student

Methods:
- def __init__(self, first_name, last_name, age):
  - instantiation of first_name, last_name, age
- def to_json(self):
  - retrieve a dictionary repr of a Student (class) instance
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

    def to_json(self):
        """
        return a reprs of a dictionary
        """
        return self.__dict__
