#!/usr/bin/python3


def user_name(email):
    username = email.split("@")[0]
    return username


email = "ben@gmail.com"
print(user_name(email))
