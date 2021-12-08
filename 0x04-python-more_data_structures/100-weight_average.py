#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    return the average weight of all ints inside every tuple in the list
    """
    if len(my_list) == 0:
        return 0

    if my_list:
        return(sum(first * second for first, second in my_list) /
               sum(second for first, second in my_list))
    else:
        return 0
