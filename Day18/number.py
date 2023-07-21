#!/usr/bin/python3


def any_number(*a):
    return sum(a)/len(a)


a = [12, 90]
print(any_number(*a))
