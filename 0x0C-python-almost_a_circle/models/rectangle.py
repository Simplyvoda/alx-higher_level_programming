#!/usr/bin/python3
"""
this module contains the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """this class inherits from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        self.__width = number
        if type(number) is not int:
            raise TypeError("width must be an integer")
        if number <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, number):
        """setter for height"""
        self.__height = number
        if type(number) is not int:
            raise TypeError("height must be an integer")
        if number <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, number):
        """setter for x"""
        self.__x = number
        if type(number) is not int:
            raise TypeError("x must be an integer")
        if number < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, number):
        """setter for y"""
         self.__y = number
        if type(number) is not int:
            raise TypeError("y must be an integer")
        if number < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """function to return area of rectangle"""
        return self.__width*self.__height

    def display(self):
        """function that prints to stdout # character"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """this function returns the informal string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                self.__x,self.__y,self.__width,self.__height)

    def update(self, *args, **kwargs):
        """this function assigns an argument to each attribute"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
