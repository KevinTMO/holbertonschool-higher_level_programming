#!/usr/bin/python3
"""
Module: 2-append_write

Method:
- def append_write(filename="", text=""):
  - appends a string at the end of a text file using UTF8 format
  ... return the number of characters
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    """
    with open(filename, 'a', encoding='UTF-8') as File:
        # appendFile = File.write(text)
        # return appendFile
        return File.write(text)
