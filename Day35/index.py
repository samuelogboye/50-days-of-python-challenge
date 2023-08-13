#!/usr/bin/python3


def find_index(a, b):
    """Takes two arguments
          a - list of integers
          b - an integer
    return indexes of integer in the list
    """
    new_list = []
    if b in a:
        for index, num in enumerate(a):
            if num == b:
                new_list.append(index)
        return new_list
    for num in range(len(a)):
        new_list.append(b)
    return new_list


print(find_index([1, 2, 4, 6, 7, 7], 7))
print(find_index([1, 2, 4, 6, 7, 7], 8))
