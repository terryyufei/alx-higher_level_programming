#!/usr/bin/python3

"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """To retrieve attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Get area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Get perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Sets the print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets the del behavior of the Rectangle object."""
        print("Bye rectangle...")
