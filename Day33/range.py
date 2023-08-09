#!/usr/bin/python3

import timeit


def time_set():
    a = range(10000000)
    x = set(a)
    for num in x:
        if num == 999:
            return True


def time_list():
    a = range(10000000)
    y = list(a)
    for num in y:
        if num == 999:
            return True


"""
start_time_set = time.time()
time_set()
end_time_set = time.time()
elapsed_time_set = end_time_set - start_time_set
print(elapsed_time_set)

start_time_list = time.time()
time_list()
end_time_list = time.time()
elapsed_time_list = end_time_list - start_time_list
print(elapsed_time_list)
"""
elapsed_time_set = timeit.timeit(time_set, number=100)
print(elapsed_time_set)
elapsed_time_list = timeit.timeit(time_list, number=100)
print(elapsed_time_list)


if elapsed_time_set < elapsed_time_list:
    print("Set is faster.")
elif elapsed_time_set > elapsed_time_list:
    print("List is faster.")
else:
    print("Both Set and List took same time.")
