#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5 and number < 10:
    ldgt = number % 10
    print(f"Last digit of {number:d} is {ldgt:d} and greater than 5")
elif number < 5:
    ldgt = number % 10
    print(f"Last digit of {number:d} is {ldgt:d} and is less than 6 and not 0")
else:
    while number > 10:
        ldgt = number % 10
if ldgt > 5:
    print(f"Last digit of {number:d} is {ldgt:d} and greater than 5")
elif ldgt == 0:
    print(f"Last digit of {number:d} is {ldgt:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ldgt:d} and is less than 6 and not 0")
