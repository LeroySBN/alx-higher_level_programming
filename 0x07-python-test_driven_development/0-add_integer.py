#!/usr/bin/python3
"""
Module 0-add_integer
Defines a sum function

"""


def add_integer(a, b=98):
    """
    Sum function add_integer that returns sum of a and b

    Args:
        a (int): first value
        b (int): second value

    Returns:
        sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif not a:
        raise TypeError("a must be an integer")
    else:
        sum = int(a) + int(b)
    return sum
