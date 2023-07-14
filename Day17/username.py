#!/usr/bin/python3
import random


def user_name():
    name = input("Enter your name: ")
    name = name.replace(" ", "")
    reversed_name = name[:: -1]
    number = random.randint(0, 9)
    username = reversed_name + str(number)
    print("Your username is ", username)


user_name()
