#!/usr/bin/python3

"""The module is 9-rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """initialize private attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of a rectangle and overrides area() from superclass"""
        return self.__width * self.__height
    
    def __str__(self):
        """Returns a human readable string representation"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))