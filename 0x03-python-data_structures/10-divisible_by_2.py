#!/usr/bin/python3
# Finds all multiples of 2 in a list


def divisible_by_2(my_list=[]):
    """
    Will find all numbers divisible by 2
    my_list: is a list of integers
    """
    if len(my_list) > 0:

        newList = []

        for checkNum in my_list:
            if checkNum % 2 == 0:
                newList.append(True)
            else:
                newList.append(False)

        return newList
