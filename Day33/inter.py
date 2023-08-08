#!/usr/bin/python3


def inter_section(list_one, list_two):
#    return (set(list_one)&set(list_two))
    return tuple([x for x in list_one if x in list_two])

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))
