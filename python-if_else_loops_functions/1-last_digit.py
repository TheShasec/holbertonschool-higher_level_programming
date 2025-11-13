#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0
if number < 0:
    last = int(str(number)[-1])*-1
else:
    last = int(str(number)[-1])
text = f"Last digit of {number} is {last} "
if last > 5:
    text = text +  "and is greater than 5"
if last == 0:
    text = text + "and is 0"
if last != 0 and last < 6:
    text = text + "and is less than 6 and not 0"
print(text)
