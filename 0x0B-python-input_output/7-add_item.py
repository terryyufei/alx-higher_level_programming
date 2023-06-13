#!/usr/bin/python3
""""adds all arguments to a Python list"""

import sys
from unicodedata import name

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    name = "add_item.json"
    arg = sys.argv[1:]

    try:
        a = load_from_json_file(name)

    except FileNotFoundError:
        a = []

    a.extend(arg)
    save_to_json_file(a, name)
