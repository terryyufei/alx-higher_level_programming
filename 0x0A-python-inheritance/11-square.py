#!/usr/bin/python3

"""importing Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

"""Write a class square that inherites from rectangle"""


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """initialize private attribute size and validate it"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return and print the square description"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
