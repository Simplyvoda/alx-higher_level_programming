#!/usr/bin/python3
"""
this module defines the Base class
"""

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
