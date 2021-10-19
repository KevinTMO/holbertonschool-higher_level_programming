#!/usr/bin/python3
"""
Module base

Class: Base
- this will be the base class for every other class
"""


import json


class Base:
    """
    Creating a class attrs there's no id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is something (not NONE) then assign attr id
        else just increment nb_object (number of objects)
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    #  json methods


    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            list_dictionaries = []
