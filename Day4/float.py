#!/usr/bin/python3

def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    if isinstance(a, float) or isinstance(b, float):
        return 1


print(only_floats(12.1, 23))
