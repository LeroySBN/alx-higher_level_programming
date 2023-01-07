#!/usr/bin/python3
"""
Module 0-add_integer
Defines a sum function

"""


def add_integer(a, b=98):
    """
    Sum function add_integer that returns sum of a and b

    Args:
        a (int): arg 1
        b (int): arg 2
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif:
        if type(a) is int and type(b) is int:
            return int(a + b)
        else:
            return (a + b)
