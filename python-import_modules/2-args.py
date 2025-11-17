#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    myl = len(args)
    if myl-1 == 0:
        print("{} arguments.".format(myl-1))
    else:
        if myl-1 == 1:i
            print("{} argument:".format(myl-1))
        else:
            print("{} arguments:".format(myl-1))
        for i in range(1, myl):
            print("{}: {}".format(i, args[i]))
