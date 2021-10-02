#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Return the real number of elements printed
    """
    counter = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end="")
        except IndexError:
            continue
        counter += 1
    print("")
    return counter
