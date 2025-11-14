#!/usr/bin/python3
x=""
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    x = x + "{}".format(chr(i))
print(x)
