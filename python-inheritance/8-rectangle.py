#!/usr/bin/python3
"""3323"""


import BaseGeometry from "7-base_geometry"
class Rectangle(BaseGeometry):
    """43434"""

    def __init__(self, width, height):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if not hasattr(self, 'width'):
            raise AttributeError("'Rectangle' object has no attribute 'width'")
        if not hasattr(self, 'height'):
            raise AttributeError("'Rectangle' object has no attribute 'height'")
