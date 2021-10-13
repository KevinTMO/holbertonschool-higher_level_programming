#!/usr/bin/python3
"""
Module: 8-class_to_json

Method:
- class_to_json
  - Return a dictionary description with simple data structure
  ... of an object for JSON serialization using __dict__
"""


def class_to_json(obj):
    """
    Return a dictionary description with simple data structure
    """
    return obj.__dict__
