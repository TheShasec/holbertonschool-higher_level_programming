#!/usr/bin/python3
"dsafdfdsf"


class Rectangle:
    "dafsdf"

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, vl):
        if not isinstance(vl, int):
            raise TypeError("width must be >= 0")
        if vl < 0:
            raise ValueError("ValueError")
        self.__width = vl
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, vl):
        if not isinstance(vl, int):
            raise TypeError("height must be an integer")
        if vl < 0:
            raise ValueError("height must be >= 0")
        self.__height = vl

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
