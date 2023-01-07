#!/usr/bin/python3
"""
Module 0-add_integer
Defines a sum function

"""


def add_integer(a, b=98):
    """
    Sum function add_integer that returns sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return a + b
