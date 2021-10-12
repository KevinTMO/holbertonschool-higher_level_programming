#!/usr/bin/python3
"""
Module 1-my_list

Methods:
- def print_sorted(self)
  - print a sorted list
"""


class MyList(list):

    def print_sorted(self):
        """
        Print a sorted list of integers (not any other type)
        """
        print(sorted(self))
