#!/usr/bin/python3
"""
Module: 4-square.py

Add a new instance attr named position
Create a getter/setter for it
Print whitespace if value is 0 in position[0] and don't if position[1] is > 0

Class:
- Square():

Instance attr:
- size (private)

Methods:
- __init__()
- area()
- size(self) -> getter
- size(self, value) -> setter
  - Will validate now instead of __init__
- my_print(self)

Validation:
- If size is an integer then assign the value
  - If not then just raise a TypeError or ValueError with a msg
"""


class Square:
    """
    Method:
    - __init__()
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instance attrs:
        - size (private)
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Get the area of a square and return it
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter will return size after setter
        Getter use "property" decorator
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter will set the value for size before retrieve it
        Now will validate too if it is an int or greater/eq than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter will return position after setter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter will set the value for position before retrieve it
        It will validate if it is an int or greater/eq than 0
        """
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Print a square using # by size until range(size)
        """
        if self.__size == 0:
            pass

        else:
            print("\n" * self.__position[1], end="")
            print('\n'.join(" " * self.__position[0] +
                            "#" * self.__size for sq in range(self.__size)))
