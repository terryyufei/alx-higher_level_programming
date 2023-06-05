# More Classes and Objects

*TASK ZERO*
> Write an empty class Rectangle that defines a rectangle:
> You are not allowed to import any module

*TASK ONE*
>Real definition of a rectangle

> Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
> Private instance attribute: width:
> property def width(self): to retrieve it
> property setter def width(self, value): to set it:
> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
> if width is less than 0, raise a ValueError exception with the message width must be >= 0

> Private instance attribute: height:
> property def height(self): to retrieve it
> property setter def height(self, value): to set it:
* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
* if height is less than 0, raise a ValueError exception with the message height must be >= 0

> Instantiation with optional width and height: def __init__(self, width=0, height=0):
> You are not allowed to import any module

*TASK TWO*
> Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

> Private instance attribute: width:
> property def width(self): to retrieve it
> property setter def width(self, value): to set it:
> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
> if width is less than 0, raise a ValueError exception with the message width must be >= 0

> Private instance attribute: height:
> property def height(self): to retrieve it
> property setter def height(self, value): to set it:
> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
> if height is less than 0, raise a ValueError exception with the message height must be >= 0
> Instantiation with optional width and height: def __init__(self, width=0, height=0):
> Public instance method: def area(self): that returns the rectangle area

> Public instance method: def perimeter(self): that returns the rectangle perimeter:
> if width or height is equal to 0, perimeter is equal to 0
> You are not allowed to import any module

*TASK THREE*
> Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

> Private instance attribute: width:
> property def width(self): to retrieve it
> property setter def width(self, value): to set it:
> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
> if width is less than 0, raise a ValueError exception with the message width must be >= 0

> Private instance attribute: height:
> property def height(self): to retrieve it
> property setter def height(self, value): to set it:
> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
> if height is less than 0, raise a ValueError exception with the message height must be >= 0
> Instantiation with optional width and height: def __init__(self, width=0, height=0):
> Public instance method: def area(self): that returns the rectangle area

> Public instance method: def perimeter(self): that returns the rectangle perimeter:
> print() and str() should print the rectangle with the character #: (see example below)
> if width or height is equal to 0, return an empty string
> if width or height is equal to 0, perimeter is equal to 0
> You are not allowed to import any module

*Task four*
> Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

> Private instance attribute: width:
> property def width(self): to retrieve it
> property setter def width(self, value): to set it:
> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
> if width is less than 0, raise a ValueError exception with the message width must be >= 0

> Private instance attribute: height:
> property def height(self): to retrieve it
> property setter def height(self, value): to set it:
> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
> if height is less than 0, raise a ValueError exception with the message height must be >= 0
> Instantiation with optional width and height: def __init__(self, width=0, height=0):
> Public instance method: def area(self): that returns the rectangle area

> Public instance method: def perimeter(self): that returns the rectangle perimeter:
> print() and str() should print the rectangle with the character #: (see example below)
> if width or height is equal to 0, return an empty string
> if width or height is equal to 0, perimeter is equal to 0
> repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
> You are not allowed to import any module

*TASK 5*
> ALL the instructions in task 4, plus
> Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

*TASK 6*
> ALL the instructions in task 5, plus
> Public class attribute number_of_instances:
> Initialized to 0
> Incremented during each new instance instantiation
> Decremented during each instance deletion

*TASK 7*
> ALL the instructions in task 6, plus
> Public class attribute print_symbol:
> Initialized to #
> Used as symbol for string representation
> Can be any type

*TASK 8*
> ALL the instructions in task 6, plus
> Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
> rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle

> rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
> Returns rect_1 if both have the same area value

*TASK 9*
> ALL the instructions in task 7, plus
> Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

