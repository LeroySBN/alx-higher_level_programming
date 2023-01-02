#!/usr/bin/python3
"""
Module 3-say_my_name
Defines a print function

"""


def say_my_name(first_name, last_name=""):
    """
    Prints name
    """
    if type(first_name) is not str or first_name == "" or first_name == " ":
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str or last_name == " ":
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
