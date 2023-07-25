#!/usr/bin/python3


def unique_numbers(a_list):
    new_list = a_list.copy()
    new_list = list(set(new_list))
    difference = sum(a_list) - sum(new_list)
    if difference % 2 == 0:
        return a_list
    return new_list


old_list = [1, 2, 4, 5, 6, 7, 8, 8]
new_list = unique_numbers(old_list)
print('Old_list ', old_list)
print('New_list ', new_list)
