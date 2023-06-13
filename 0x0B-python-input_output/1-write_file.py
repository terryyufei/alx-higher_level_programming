#!/usr/bin/python3

"""Write a string from a textfile"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, 'w') as file:
        return file.write(text)
