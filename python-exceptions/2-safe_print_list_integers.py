#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except:
            pass
        t = t + 1
    print()
    return t
