#!/usr/bin/python3
"""343"""


class BaseGeometry:
    """3232"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise f"{name} must be an integer"
        if value <= 0 :
            raise f"{name} must be greater than 0"

