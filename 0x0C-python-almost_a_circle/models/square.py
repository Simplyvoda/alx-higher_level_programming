#!/usr/bin/python3
"""
This module contains the Square class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """this represents a square"""
    def __init___(self, size, x=0, y=0, id=None):
        """this initialises the class square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size argument, width and height are equal"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({id}) {x}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """function to update attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Square"""
        dic_nary = {}
        dic_nary["id"] = self.id
        dic_nary["size"] = self.size
        dic_nary["x"] = self.x
        dic_nary["y"] = self.y
        return dic_nary




