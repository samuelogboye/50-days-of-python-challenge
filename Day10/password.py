#!/usr/bin/python3


def hide_password():
    password = input("Enter a password: ")
    lenght = len(password)
    print("*"*lenght)
    print("The password is {} characters long.".format(lenght))


hide_password()
