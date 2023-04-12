#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """The class implement sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
