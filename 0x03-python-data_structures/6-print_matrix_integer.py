#!/usr/bin/python3
# Print a matrix of integers


def print_matrix_integer(matrix=[[]]):
    """
    Will print a matrix of integers
    matrix: is the matrix to print
    """
    for newMatrix in matrix:
        print(" ".join("{:d}".format(idx) for idx in newMatrix))
