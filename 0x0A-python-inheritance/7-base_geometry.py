#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Create a BaseGeometry instance"""
    def area(self):
        """Unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater that 0")
