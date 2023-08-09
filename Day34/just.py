#!/usr/bin/python3
import csv


def just_digits():
    new_list = []
    with open("python.csv", "r") as file:
        read_file = file.read()
        read_file = read_file.split()
        for item in read_file:
            if item.isdigit():
                new_list.append(item)
        print(new_list)


just_digits()
