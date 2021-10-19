#!/usr/bin/python3
"""
Module: square

BaseClass: Base
ParentClass: Rectangle

Square class will inherit from Rectangle

Attrs:
- size
- x
- y
- id (called from Rectangle)

Constructor: __init__(self, size, x=0, y=0, id=None)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call super() to use Rectangle attrs
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    #  __str__ method return a string of Square

    def __str__(self):
        """
        Overload __str__ method
        Using attrs when calling super().__init__
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.size)

    #  getter methods (return value from width)

    @property
    def size(self):
        """
        return self.__size value after set value
        """
        return self.width

    #  setter methods (set value for width, height)

    @size.setter
    def size(self, value):
        """
        set values for size
        """
        self.width = value
        self.height = value

    #  args & kwargs method

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
                    self.size = value
                if index == 2:
                    self.x = value
                if index == 3:
                    self.y = value

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
        """
        returns a dictionary representation
        First declare a variable a assign an empty dictionary
        then create the dictionary using all attrs values
        """
        #  newDict = {}
        #  newDict["id"] = self.id
        #  newDict["size"] = self.size
        #  newDict["x"] = self.x
        #  newDict["y"] = self.y
        #  return newDict
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
