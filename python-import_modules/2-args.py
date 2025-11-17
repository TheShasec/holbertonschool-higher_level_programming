#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    l = len(args)
    if l-1 == 0:
        print("{} arguments.".format(l-1))
    else:
        if l-1 == 1:
            print("{} argument:".format(l-1))
        else:
            print("{} arguments:".format(l-1))
        for i in range(1,l):
            print("{}: {}".format(i,args[i]))
