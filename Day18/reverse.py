#!/usr/bin/python3


def add_reverse(a, b):
    if len(a) == len(b):
        b = a+b
        return sorted(b)
    else:
        return a+b


a = [10, 12, 34]
b = [12, 56, 78]
print(add_reverse(a, b))
