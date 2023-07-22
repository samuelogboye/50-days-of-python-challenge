#!/usr/bin/python3


def add_hash(string):
    return string.replace(" ", "#")


def add_underscore(string):
    return string.replace("#", "_")


def remove_underscore(string):
    return string.replace("_", "")


print(remove_underscore(add_underscore(add_hash('Python'))))
