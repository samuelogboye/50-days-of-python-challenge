#!/usr/bin/python3


def longest_value(my_dict):
    longest = None
    for value in my_dict.values():
        if longest is None or len(value) > len(longest):
            longest = value
    return longest


fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))
