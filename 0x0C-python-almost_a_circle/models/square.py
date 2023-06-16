#!/usr/bin/python3

from models.base import Base
from models.rectangle import Rectangle

"""Write a child class Square"""


class Square(Rectangle):
    """
    A subclass of class Rectangle
    args:
        size: size
        x: position
        y: position
        id: id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of a square instance"""
        return "[square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieve attribute from class Rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """validation from class Rectangle"""
        self.width = value
        self.height = value
