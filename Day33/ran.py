#!/usr/bin/python3

import timeit


def time_set():
    a = range(100000000)
    x = set(a)
    for num in x:
        if num == 9999:
            return True


def time_list():
    a = range(100000000)
    y = list(a)
    for num in y:
        if num == 9999:
            return True


set_time = timeit.timeit(time_set, number=100)
list_time = timeit.timeit(time_list, number=100)

print("Set time:", set_time)
print("List time:", list_time)
