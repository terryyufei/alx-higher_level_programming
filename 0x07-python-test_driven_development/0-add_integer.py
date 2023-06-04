#!/usr/bin/python3

"""
The module is add_interger
It adds two intergers together
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b
    Args:
        a(int, float) the first value
        b(int, float) the second value
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
