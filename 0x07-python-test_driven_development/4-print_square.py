#!/usr/bin/python3

"""
The module is print_square
It prints a square with the character #
"""


def print_square(size):
    """
    prints a square where size is the length of the square
    args:
        size(int) : length of square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float or size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
