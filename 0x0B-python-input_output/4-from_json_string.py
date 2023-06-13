#!/usr/bin/python3

"""converting from JSON string to python data structure"""

import json
"""Provides the functions needed to convert"""


def from_json_string(my_str):
    """
     function that returns an object (Python data structure)
     represented by a JSON string:
    """
    return json.loads(my_str)
