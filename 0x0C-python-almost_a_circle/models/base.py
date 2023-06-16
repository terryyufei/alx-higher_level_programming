#!/usr/bin/python3

"""Write the first class Base"""


class Base:
    """The base(super) class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
