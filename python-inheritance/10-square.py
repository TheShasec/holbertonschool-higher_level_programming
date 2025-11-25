#!/usr/bin/python3
"""34234"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """32323"""

    def __init__(self, size):
        self.integer_validator(size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
