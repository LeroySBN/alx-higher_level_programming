#!/usr/bin/python3
"""Module 4-print_square"""


def print_square(size):
    """
    prints a square with character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print("\n".join(["#" * size for i in range(size)]))
