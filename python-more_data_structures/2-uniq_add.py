#!/usr/bin/python3
def uniq_add(my_list=[]):
    at = []
    ss = 0
    for i in my_list:
        if i not in at:
            at.append(i)
            ss = ss + i
    return ss
