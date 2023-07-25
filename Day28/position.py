#!/usr/bin/python3


def index_position(string):
    new = []
    for i in string:
        if i.islower():
            new.append(string.index(i))
    return new


print(index_position('LovE'))
