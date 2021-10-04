#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    This method divides all elements in the matrix
    - Matrix should be a list of lists of int or float
    - If not then raise TypeError
    - Each row must be the same size
    - If not then raise TypeError
    - Div must be a number (int, float)
    - If not then raise TypeError
    - Div can't be 0
    - Otherwise raise ZeroDivisionError
    - Return Matrix
    """
    Notlst = 'matrix must be a matrix (list of lists) of integers/floats'
    NotSize = 'Each row of the matrix must have the same size'

    if not isinstance(matrix, list):
        raise TypeError(Notlst)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    xPos = len(matrix[0])

    for row in matrix:
        if xPos != len(row):
            raise TypeError(NotSize)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(Notlst)
        if not isinstance(row, list):
            raise TypeError(Notlst)
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(Notlst)

    return [[round(value / div, 2) for value in row] for row in matrix]
