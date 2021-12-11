#!/usr/bin/python3
"""
Module 8-rectangle.py

Create a new method to compare the area of two rectangles and return the bgest

Class:
- Rectangle:

Attrs:
- width (priv)
- height (priv)
- number_of_instances (class atrs/public)
- print_symbol (class atrs/public)

Methods:
- __init__()
- def width(self) / def width(self, value)
- def height(self) / def height(self, value)
- def area(self)
- def perimeter(self)
   - if width or height == 0 then perimeter is == 0
- def __str__(self)
- def __repr__(self)
- def __del__(self)
- def bigger_or_equal(rect_1, rect_2)

Decorators:
- @property
- @setter
- @staticmethod
"""


class Rectangle:
    """
    Will get the width/height of a rectangle
    Attr:
    - number_of_instances (public)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initiate objects with attrs width/height
        Assign each attr with a value
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter of width attr to return the value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of width attr will set width with a value
        Validate if width is int or is greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter of heigth attr to return the value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height attr will set height with a value
        Validate if height is int or is greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """
        Return the area of a rectangle using height + width
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of a rectangle using heigth + width
        if height or width are == 0 then perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string rep of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        else:
            return ('\n'.join(str(self.print_symbol) * self.__width for rc in
                              range(self.__height)))

    def __repr__(self):
        """
        Return a string rep of the object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Return a string msg when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest area of the two rectangles after compare
        Validate if rect_1 and rect_2 are instances of Rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
