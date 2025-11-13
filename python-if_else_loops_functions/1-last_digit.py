#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
first = f"Last digit of {number} "
if number < 0:
    first -= f"is -{str(number)[-1]} "
else:
    first += f"is {str(number)[-1]} "
if int(str(number)[-1])>5:
    first = first + "and is greater than 5"
elif int(str(number)[-1])>5:
    first = first + "and is 0"
else:
    first = first + "and is less than 6 and not 0"
print(first)
