#!/usr/bin/python3

"""
The module is say_my_name
It prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first name> <last name>.
    Args:
        first_name(string) the first value
        last_name(string) the second value
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
