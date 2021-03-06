#!/usr/bin/python3
"""
Module: 0-read_file

Method:
- def read_file(filename=""):
  - read a text file in UTF8 format and prints to stdout
"""


def read_file(filename=""):
    """
    Read a text file and prints to stdout
    """
    with open(filename, encoding='UTF-8') as File:
        print(File.read(), end="")
