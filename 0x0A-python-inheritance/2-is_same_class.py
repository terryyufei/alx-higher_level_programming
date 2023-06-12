#!/usr/bin/python3

"""The module is 2-is_same_class"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class
    Returns True if the object is exactly an instance of the specified class
    Returns False otherwise
    """
    return type(obj) is a_class
