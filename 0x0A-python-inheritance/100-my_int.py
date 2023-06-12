#!/usr/bin/python3

"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """A subclass of class int"""
    def __eq__(self, other):
        """sets the behaviour of == """
        return int(self) != other

    def __ne__(self, other):
        """sets the != behavior"""
        return int(self) == other
