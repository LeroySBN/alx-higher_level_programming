#!/usr/bin/python3
"""
Module 6-square
Defines a class 'Square'

"""


class Square:
    """
    Defines a Square instance.

    Args:
            size (int): size of the square

    """

    def __init__(self, size=0, position=(0,0)):
        """The Square __init__ method initializes the attribute 'size'.

        Args:
            size (int): size of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Square getter method.

        Returns:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Square setter method.

        Args:
            value (int): sets size to value

        Raises:
            TypeError: If value is not integer
            ValueError: If value is less than 0

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Square area method.

        Returns:
            Area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self._position:
                        for k in range(self._position[0]):
                            print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """Square getter method for position"""
        return self._position

    @position.setter
    def position(self, value):
        if (len(value) != 2) and (type(value[0]) is not int) and (value[0] < 0) and (type(value[1]) is not int) and (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value
