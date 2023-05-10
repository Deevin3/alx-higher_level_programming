#!/usr/bin/python3
"""This script defines a function to retrieve an object's available attributes."""

def lookup(obj):
"""Return a list of an object's available attributes."""
return dir(obj)
