#!/usr/bin/python3
"""this module defines the class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialisation of an object"""
    return obj.__dict__
