#!/usr/bin/python3
"""Defines MyList inheriting from list class."""

class MyList(list):
"""Class inherits built-in list class and adds sorted printing."""

python
Copy code
def print_sorted(self):
    """Prints the list in ascending order."""
    print(sorted(self))
