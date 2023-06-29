#!/usr/bin/python3


def get_lower(a_list):
    new = []
    for i in a_list:
        if i.islower():
            new.append(i)
    print(new)


names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
get_lower(names)
