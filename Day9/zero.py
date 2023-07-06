#!/usr/bin/python3


def zeros_last(a_list):
    """a function that takes a list as argument
    if the list has zeros it will move them to the front of
    the listand maintain the order of the other numbers in the list.
    If there are no Zeros in the list, the function should return the
    original list sorted in ascending order
    """
    if 0 in a_list:
        a_list = [x for x in a_list if x != 0] + [x for x in a_list if x == 0]
    else:
        a_list.sort()
    return a_list


l1 = [2, 1, 4, 7, 6]
l2 = [1, 4, 6, 0, 7, 0, 9]
print(zeros_last(l1))
print(zeros_last(l2))
