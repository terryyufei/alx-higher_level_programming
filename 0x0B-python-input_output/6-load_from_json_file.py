#!/usr/bin/python3

"""Create an object from a JSON file"""

import json
"""Provides the functions needed for converting"""


def load_from_json_file(filename):
    """a function that creates an Object from a 'JSON file'"""
    with open(filename) as file:
        return json.load(file)
