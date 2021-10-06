#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    This method should print only integers of a list
    my_list: is a list of mixed types elements
    x: is the number of elements to be printed
    Only integers should be print. Ignore any other type.
    If the number (x) to print of elements is bigger than len -> error
    Should use an exception error for that statement -> IndexError
    """
    count = 0

    for index in range(x):

        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
