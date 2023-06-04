#!/usr/bin/python3

"""
The module is matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    Args:
    matrix(list) :  list of lists of integers or floats.
    div(int, float) : divider >= 0
    """
    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error)
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error)
    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for n in matrix[i]:
            if type(n) is int or type(n) is float:
                new_matrix[i].append(round(n / div, 2))
            else:
                raise TypeError(error)
    return new_matrix
