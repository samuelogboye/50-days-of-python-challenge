#!/usr/bin/python3

def missing_numbers(a_list):
    """A function that takes a list of sequence of numbers
    and finds the missing numbers in the sequence"""
    a_list.sort()
    missing = []
    for num in range(a_list[0], a_list[-1]):
        if num not in a_list:
            missing.append(num)
    return missing


a = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
     18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

print(missing_numbers(a))
