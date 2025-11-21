#!/usr/bin/python3 
ro = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
roa = ['I', 'V', 'X', 'L', 'C', 'D', 'M',]
def check(fi, la):
    if roa.index(fi) >= roa.index(la):
        return True
    else:
        return False


def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string is None:
        return 0
    su = 0
    if len(roman_string) == 1:
        return su + ro[roman_string[0]]
    for i in range(len(roman_string)-1):
        if check(roman_string[i], roman_string[i+1]):
            su += ro[roman_string[i]]
        else:
            su -= ro[roman_string[i]]
    su += ro[roman_string[-1]]
    return su
