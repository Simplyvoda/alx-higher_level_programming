#!/usr/bin/python3
"""this module defines the save_to_json function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to the text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
