#!/usr/bin/python3
# Get the square value of all integers in the matrix


def square_matrix_simple(matrix=[]):
    """
    matrix: is a two dimension array
    """
    return [[num ** 2 for num in newMatrix] for newMatrix in matrix]
