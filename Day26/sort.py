#!/usr/bin/python3


def sort_words(string):
    string = string.replace(" ", "")
    unique = set()
    for i in string:
        unique.add(i)
    return sorted(unique)


print(sort_words('love life'))
