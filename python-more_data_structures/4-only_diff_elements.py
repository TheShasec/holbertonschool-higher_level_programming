#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ms = []
    s1 = list(set_1)
    s2 = list(set_2)
    for i in s1:
        if s2.count(i) == 0:
            ms.append(i)
    for i in s2:
        if s1.count(i) == 0:
            ms.append(i)
    return set(ms)
