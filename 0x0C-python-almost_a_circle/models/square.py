#!/usr/bin/python3

"""Write a child class Square"""

from models.rectangle import Rectangle


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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieve attribute from class Rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """validation from class Rectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
            }
