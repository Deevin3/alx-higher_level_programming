#!/usr/bin/python3
"""This function checks if an object is exactly an instance of a given class."""

def is_same_class(obj: any, a_class: type) -> bool:
"""
Args:
obj: The object to check.
a_class: The class to match the type of obj to.
Returns:
True if obj is exactly an instance of a_class. Otherwise, False.
"""
return True if type(obj) == a_class else False
