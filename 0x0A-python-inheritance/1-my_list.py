#!/usr/bin/python3

"""The module is 1-my_list"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
