#!/usr/bin/python3

"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """
     a function that inserts a line of text to a file,
     after each line containing a specific string
      Args:
        - filename: name of the file
        - search_string: string to append after
        - new_string: new_string to append
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        fo.write(string)
