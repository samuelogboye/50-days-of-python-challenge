#!/usr/bin/python3

def count(a_string):
    a_dict = {}
    for letter in a_string:
        if letter in a_dict:
            a_dict[letter] += 1
        else:
            a_dict[letter] = 1

    return a_dict


input_string = "hello"
result = count(input_string)
print(result)
