#!/usr/bin/python3
"""Module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method for square instance"""
        super().__init__(size, size, x, y)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of rectangle instance"""
        str_rep = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return str_rep

    def update(self, *args, **kwargs):
        """Instance method that updates the rectangle"""
        if *args is None:
            self.width = kwargs['id']
            self.height = kwargs['size']
            self.x = kwargs['x']
            self.y = kwargs['y']
        else:
            self.width = args.id
            self.height = args.size
            self.x = args.x
            self.y = args.y

    def to_dictionary(self):
        """Dictionary representation of rectangle instance"""
        dic_rep = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
        return dic_rep
