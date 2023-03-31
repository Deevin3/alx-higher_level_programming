#!/usr/bin/python3
"""A module for working with squares."""

class Square:
"""Represents a 2D square."""

def __init__(self, size=0, position=(0, 0)):
    """Initializes a Square with a given size and position."""
    self.size = size
    self.position = position

@property
def size(self):
    """Gets the size of the Square object."""
    return self.__size

@size.setter
def size(self, value):
    """Sets the size of the Square object."""
    if not isinstance(value, int):
        raise TypeError('size must be an integer')
    elif value < 0:
        raise ValueError('size must be >= 0')
    else:
        self.__size = value

@property
def position(self):
    """Gets the position of the Square object."""
    return self.__position

@position.setter
def position(self, value):
    """Sets the position of the Square object."""
    if not isinstance(value, tuple) or len(value) != 2 \
            or not isinstance(value[0], int) or not isinstance(value[1], int) \
            or value[0] < 0 or value[1] < 0:
        raise TypeError('position must be a tuple of 2 positive integers')
    else:
        self.__position = value

def area(self):
    """Returns the area of the Square object."""
    return self.__size ** 2

def my_print(self):
    """Prints the Square object."""
    if self.__size == 0:
        print()
    else:
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for column in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
