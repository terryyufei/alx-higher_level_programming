#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    tri = []
    if n <= 0:
        return tri
    if n == 0:
        return [[1]]

    tri = [[1]]
    for i in range(n-1):
        tri.append([a+b for a, b in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
