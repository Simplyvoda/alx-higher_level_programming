#!/usr/bin/python3
"""
this module contains the rectangle class
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

class Rectangle(Base):
    """this class inherits from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the rectangle class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @width.setter
    def width(self, number):
        """setter for width"""
        if type(number) is not int:
            raise TypeError("width must be an integer")
        if number <= 0:
            raise ValueError("width must be > 0")
        self.__width = number

    @height.setter
    def height(self, number):
        """setter for height"""
        if type(number) is not int:
            raise TypeError("height must be an integer")
        if number <= 0:
            raise ValueError("height must be > 0")
        self.__height = number

    @x.setter
    def x(self, number):
        """setter for x"""
        if number < 0:
            raise ValueError("x must be >= 0")
        self.__x = number

    @y.setter
    def y(self, number):
        """setter for y"""
        if number < 0:
            raise ValueError("y must be >= 0")
        self.__y = number

    def area(self):
        """function to return area of rectangle"""
        return self.__width*self.__height
