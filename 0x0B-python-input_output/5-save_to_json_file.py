#!/usr/bin/python3
"""
Module: 5-save_to_json_file

Method:
- def save_to_json_file(my_obj, filename):
  - Save an object in a open file with write permission
  ... using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    """
    with open(filename, 'w', encoding="UTF-8") as File:
        return json.dump(my_obj, File)
