#!/usr/bin/python3
"""this module has the MyList class"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
