#!/usr/bin/python3


def your_age():
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    name = input("Input your name: ")
    name = name.lower()
    key = names_age.get(name, "error")
    if key == "error":
        print("Ops your name is not in the dictionary")
        new_age = int(input("Enter your age: "))
        names_age[name] = new_age
        key = new_age
    print("Hi, {}, you are {} years old.".format(name.capitalize(), key))
    print(names_age)


your_age()
