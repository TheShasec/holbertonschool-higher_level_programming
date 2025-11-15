#!/usr/bin/python3
def print_last_digit(number):
    try:
        a=int(number)
    except ValueError:
        print("Traceback (most recent call last):")
        return
    print(str(number)[-1],end="")
    return str(number)[-1]
