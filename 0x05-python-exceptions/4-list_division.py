#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide two lists element by element and return the result
    """
    newLst = []
    for index in range(list_length):
        result = 0
        try:
            result = my_list_1[index] / my_list_2[index]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            newLst.append(result)
    return newLst
