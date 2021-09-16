#!/usr/bin/python3
# Return mapped values to a new list



def multiply_list_map(my_list=[], number=0):
    """
    my_list: a list of integers
    number: to value to multiply each integer
    """
    if my_list:
        return list(map(lambda value: value * number, my_list))
