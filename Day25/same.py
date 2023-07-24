#!/usr/bin/python3

def all_the_same(b):
    return all(item == b[0] for item in b)


print(all_the_same(['Mary', 'Mary', 'Mary']))
