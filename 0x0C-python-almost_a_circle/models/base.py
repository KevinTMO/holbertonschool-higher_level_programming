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
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(self, list_objs):
        """
        writes the JSON string rep of list_objs to a file
        """
        objs = []

        if list_objs is not None:
            for objects in list_objs:
                objs.append(self.to_dictionary(objects))

        filename = self.__name__ + ".json"

        with open(filename, "w") as File:
            File.write(self.to_json_string(objs))
