#!/usr/bin/python3

"""Read from a file"""


def read_file(filename=""):
    """Reads text from a file and prints to stdout"""
    with open(filename) as file:
        content = file.read()
    print(content, end="")
