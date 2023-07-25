#!/usr/bin/python3


def string_length(string):
    string = string.split()
    updated_dict = {}
    for i in string:
        diic = {i: len(i)}
        updated_dict.update(diic)
    return updated_dict


print(string_length('Hi my name is Richard'))
