#!/usr/bin/python3
"""
this module defines the Base class
"""
import json
import turtle
import csv

class Base:
    """the base of other classes in project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to cls file"""
        file = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file, 'w') as f:
            f.write(cls.to_json_string(new_list)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        lo = []
        try:
            with open(file, 'r') as f:
                lo = cls.from_json_string(f.read())
            for i, a in enumerate(lo):
                lo[i] = cls.create(**lo[i])
        except:
            pass
        return lo 
