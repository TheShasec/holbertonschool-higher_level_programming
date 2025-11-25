#!/usr/bin/python3
"""4234"""

class MyList(list):
    """3323"""

    def append(self, value):
        super().append(value)

    def __str__(self):
        return super().__str__()

    def print_sorted(self):
        al = self[::]
        al.sort()
        return al
