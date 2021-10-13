#!/usr/bin/python3
"""
Module: 1-write_file

Method:
- def write_file(filename="", text=""):
  ... writes a string to a text file in UTF-8 format
  ... return the numbers of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    """
    count = 0

    with open(filename, 'w', encoding='UTF-8') as File:
        writeFile = File.write(text)
        return writeFile
        # return File.write(text)
