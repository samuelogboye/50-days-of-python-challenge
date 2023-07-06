#!/usr/bin/python3


def odd_even(a_list):
    """A function that takes a list of numbers
    and returns the difference between the max in even and
    min in odd"""
    even = []
    odd = []
    for i in a_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return max(even) - min(odd)


a = [1, 2, 4, 6]
print(odd_even(a))
