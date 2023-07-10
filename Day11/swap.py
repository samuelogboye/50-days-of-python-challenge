#!/usr/bin/python3


def swap_values(num_list):
    num_list[0], num_list[-1] = num_list[-1], num_list[0]
    return num_list


a = [2, 4, 67, 7]
print(swap_values(a))
