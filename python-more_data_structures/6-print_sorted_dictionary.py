#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tl = list(a_dictionary.keys())
    tl.sort()
    for i in tl:
        print("{}: {}".format(i, a_dictionary[i]))
