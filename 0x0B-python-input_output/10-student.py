#!/usr/bin/python3

"""Write a class"""


class Student:
    """Defines a class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes the attributes of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d[attr] = getattr(self, attr)
            return d
