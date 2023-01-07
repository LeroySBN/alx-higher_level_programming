#!/usr/bin/python3
"""
Module 3-say_my_name
Defines a print function

"""


def say_my_name(first_name, last_name=""):
    """
    Prints name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
