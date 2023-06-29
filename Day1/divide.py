#!/usr/bin/python3

import math


def divide_or_square(num):
    if num % 5 == 0:
        return round(math.sqrt(num), 2)
    else:
        return num % 5


number = int(input("Enter a number: "))
print(divide_or_square(number))
