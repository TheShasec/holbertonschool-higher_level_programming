#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new  = [::]
    for i in range(len(my_list)):
        if new[i] == search:
            new[i] = replace
    return new
