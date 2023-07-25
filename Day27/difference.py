#!/usr/bin/python3


def difference(list_one, list_two):
    return list(set(list_one) ^ set(list_two))


list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))
