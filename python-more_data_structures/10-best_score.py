#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary.keys()) == 0 or a_dictionary == None:
        return None
    tl = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == tl:
            return i
