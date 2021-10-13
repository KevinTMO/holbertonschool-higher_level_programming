#!/usr/bin/python3
"""
Module: 6-load_from_json_file

Method:
- def load_from_json_file(filename):
  - Write a function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a JSON file
    """
    with open(filename, 'r', encoding="UTF-8") as File:
        return json.load(File)
