#!/usr/bin/python3


def middle_figure(a, b):
    a += b
    a = a.replace(" ", "")
    middle_index = int((len(a) - 1) / 2)
    return a[middle_index]


str1 = "make love"
str2 = "not wars"
print(middle_figure(str1, str2))
