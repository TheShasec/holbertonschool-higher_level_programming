#!/usr/bin/python3
"""2343234"""


class Student:
    """3234"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        md = {}
        if attrs is not None:
            for i, j in self.__dict__.items():
                if i in attrs:
                    md[i] = j
            return md
        return self.__dict__
    def reload_from_json(self, json):
        ti = json[1:-1].split(",")
        for i in ti:
            key = i.split(":")[0].strip()
            value = i.split(":")[1].strip()
            self.__dict__[key] = value
