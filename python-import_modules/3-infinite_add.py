#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    result = 0
    if len(args) - 1 == 0:
        print(0)
    else:
        for i in range(1, len(args)):
            result += int(args[i])
        print(result)
