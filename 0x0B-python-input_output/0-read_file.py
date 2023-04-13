#!/usr/bin/python3
"""Define a text file-reading function."""


def read_file(filename=""):
    """Print the a text file of a UTF8 to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")