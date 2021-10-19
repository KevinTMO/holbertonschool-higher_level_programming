#!/usr/bin/python3
"""
Module: rectangle

BaseClass: Base

Class: Rectangle
- will inherit from Base

Attrs:
- width
- height
- x
- y

Methods:
__init__ (constructor, initialazing attributes)
Getters (return values after set a value on attrs)
Setters (check if the value assigned on it is what we want)
area (will return the area of a rectangle)

"""


from models.base import Base


class Rectangle(Base):
    """
    Inherit from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Assign each value to an attrs
        Call super() to get the id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #  Getters methods (returning value)

    @property
    def width(self):
        """
        getter of width
        """
        return self.__width

    @property
    def height(self):
        """
        getter of height
        """
        return self.__height

    @property
    def x(self):
        """
        getter of x
        """
        return self.__x

    @property
    def y(self):
        """
        getter of y
        """
        return self.__y

    #  Setter methods (set attributes with a value, test first)

    @width.setter
    def width(self, value):
        """
        set width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        set x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        set y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    #  Area method

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height

    #  display method to (prints) a rectangle - '#' by width and height

    def display(self):
        """
        prints a string that display a rectangle
        """
        sign = "#"
        newLine = "\n"
        #  ln = line (row)
        #  print(newLine * self.__y, end="")
        print(newLine * self.__y +
              newLine.join(" " * self.__x + sign * self.__width
                           for ln in range(self.__height)))

    #  __str__ method to return a string representation of rectangle

    def __str__(self):
        """
        return a str representation of the class
        """
        return("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height))

    #  Updated method that will updated each attrs

    def update(self, *args, **kwargs):
        """
        update an attr by assigning an arg to ea attr
        check if there's something in args
        If there's something then update each by order:
           - Order: id, width, height, x, y
        To get the order is better using enumarate to give ea a number
        If there's nothing in args then we look for keywords and assign
        a new value
        """
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.__width = value
                if index == 2:
                    self.__height = value
                if index == 3:
                    self.__x = value
                if index == 4:
                    self.__y = value

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    #  return a dictionary representation of Rectangle

    def to_dictionary(self):
        """
        returns a dictionary representation
        First declare a variable a assign an empty dictionary
        then create the dictionary using all attrs values
        """
        #  newDict = {}
        #  newDict["id"] = self.id
        #  newDict["width"] = self.width
        #  newDict["height"] = self.height
        #  newDict["x"] = self.x
        #  newDict["y"] = self.y
        #  return newDict
        return {
            "id": self.id,
            "widht": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
