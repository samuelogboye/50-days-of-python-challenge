#!/usr/bin/python3


def zeroed(a_list):
    a_list[0], a_list[-1] = 0, 0
    return a_list


a = [2, 5, 7, 8, 9]
print(zeroed(a))
