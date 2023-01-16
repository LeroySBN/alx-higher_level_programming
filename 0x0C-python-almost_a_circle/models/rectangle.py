#!/usr/bin/python3
"""Module rectangle"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method for rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Instance mehod that returns the area of a rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """Instance method that prints a rectangle in stdout"""
        if self.width == 0 or self.height == 0:
            print("")
        rw, rh = self.width self.height
        rx, ry = self.x self.y
        display_output = [f"" for y in range(ry)][f"#" * rw for i in range(rh)]
        return "{\n}".join(display_ouput)

    def __str__(self):
        """String representation of rectangle instance"""
        str_rep = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)
        return str_rep

    def update(self, *args, **kwargs):
        """Instance method that updates the rectangle"""
        if *args is None:
            self.width = kwargs['width']
            self.height = kwargs['height']
            self.x = kwargs['x']
            self.y = kwargs['y']
        else:
            self.width = args.width
            self.height = args.height
            self.x = args.x
            self.y = args.y

    def to_dictionary(self):
        """Dictionary representation of rectangle instance"""
        dic_rep = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "heigth": self.height,
            "width": self.width
            }
        return dic_rep
