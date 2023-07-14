#!/usr/bin/python3


def sum_list(a):
    sum = 0
    for element in a:
       if isinstance(element, list):
           sum += sum_list(element)
       elif isinstance(element, int):
           sum += element
    return sum


a = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(a))
