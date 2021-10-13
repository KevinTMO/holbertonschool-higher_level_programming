#!/usr/bin/python3
"""
Module: 12-pascal_triangle

Method:
- def pascal_triangle(n):
  - returns a list of lists of integers in Pascal Triangle format
"""


def pascal_triangle(n):
   one = [1]
   sumY = [0]
   for row in range(n):
      print(one)
      one = [left + right for left, right in zip(one + sumY, sumY + one)]
   return n >= 1
