#!/usr/bin/python3
"""
Module: 3-json_string

Method:
- def to_json_string(my_obj):
  - return JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    return JSON representation of an object
    """
    return json.dumps(my_obj)
