#!/usr/bin/python3

"""Write the first class Base"""

import json


class Base:
    """The base(super) class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        obj = []
        with open(cls.__name__ + ".json", 'w') as file:
            if list_objs is None:
                json.dumps(obj, file)  # save as an empty list
            else:
                for i in list_objs:
                    obj.append(i.to_dictionary())
                file.write(cls.to_json_string(obj))  # write string to file

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
