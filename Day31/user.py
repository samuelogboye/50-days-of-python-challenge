#!/usr/bin/python3


def create_user():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    password = input("Whats your password? ")

    info = {'name': name, 'age': age, 'password': password}
    print("User saved. Please login")
    while True:
        a_name = input("Re-enter your name: ")
        pass_now = input("Re-enter your password: ")
        if (a_name == info.get('name')) and (pass_now == info.get('password')):
            print("Logged in successfully")
            break
        else:
            print("Wrong password or username. Please try again")


create_user()
