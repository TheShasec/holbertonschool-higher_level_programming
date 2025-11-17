#!/usr/bin/python3
def no_c(my_string):
    ml = list(my_string)
    for i in range(0,len(ml)):
        if i == "c" or i == "C":
            ml[i] = ""
    return "".join(ml)
