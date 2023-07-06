#!/usr/bin/python3


def biggest_odd(string):
    """A function that takes a string of numbers
    and returns the biggest odd number
    in the list"""
    return max([i for i in string if int(i) % 2 != 0])


print(biggest_odd("23569"))
