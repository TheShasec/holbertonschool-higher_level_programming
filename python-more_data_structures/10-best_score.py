#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    if len(a_dictionary) == 0:
        return None
    tl = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == tl:
            return i
