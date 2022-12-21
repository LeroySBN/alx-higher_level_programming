#!/usr/bin/python3
"""Defines a class 'Square'"""


class Square:
    """Defines a Square instance"""

    def __init__(self, size=0):
        """The Square __init__ method initializes the attribute 'size'.

        Args:
            size (int): size of the square - private attribute

        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than 0

        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except:
            raise TypeError("size must be an integer")

    def square():
        """Square method.

        Args:
            None

        Returns:
            None
        """
        pass
    pass
