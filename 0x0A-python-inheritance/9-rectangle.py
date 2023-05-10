#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize  new Rectangle.
        Args:
            Width (int):  Width of the new Rectangle.
            Height (int): Height of the new Rectangle.
        """
        super().integer_validator("Width", Width)
        self.__Width = Width
        super().integer_validator("Height", Height)
        self.__Height = Height

    def area(self):
        """Return  area of the rectangle."""
        return self.__Width * self.__Height

    def __str__(self):
        """Return  print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__Width) + "/" + str(self.__Height)
        return string
