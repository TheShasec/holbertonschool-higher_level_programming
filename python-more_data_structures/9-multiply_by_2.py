#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mi = a_dictionary.copy()
    for i in mi:
        mi[i] = mi[i] * 2        
    return mi
