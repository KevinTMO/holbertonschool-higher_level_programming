#!/usr/bin/python3
# Delete a value at pos


def delete_at(my_list=[], idx=0):
    """
    Will delete an item at idx pos
    my_list: is a list of integers
    idx: is the pos to delete
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        del(my_list[idx])
        return my_list
