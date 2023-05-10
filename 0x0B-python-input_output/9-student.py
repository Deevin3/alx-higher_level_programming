#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, name1, name2, age):
        """Initialize a new Student.
        Args:
            name1 (str): first name of the student.
            name2 (str):  last name of the student.
            age (int):  age of the student.
        """
        self.name1 = name1
        self.name1 = name2
        self.age = age

    def to_json(self):
        """Get dictionary representation of Student."""
        return self.__dict__
