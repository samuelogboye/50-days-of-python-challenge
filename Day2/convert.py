#!/usr/bin/python3


def convert_add(a_list):
    new_list = []
    sum = 0
    for i in a_list:
        new_list.append(int(i))
        sum += int(i)
    print("New List:", new_list)
    print("The sum:", sum)


a = ['1', '3', '5']
convert_add(a)
