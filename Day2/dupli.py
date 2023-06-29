#!/usr/bin/python3


def check_duplicates(a_list):
    for i in a_list:
        str_count = a_list.count(i)
    if str_count > 1:
        print(i)
    else:
        print("No duplicates")


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
check_duplicates(fruits)
check_duplicates(names)
