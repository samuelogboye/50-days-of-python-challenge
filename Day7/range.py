#!/usr/bin/python3


def string_range(num):
    output = ""
    for i in range(num):
        if i == num - 1:
            output += str(i)
        else:
            output += str(i) + "."
    return output


print(string_range(6))
