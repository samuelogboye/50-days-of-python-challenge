#!/usr/bin/python3

import json


def save_json():
    names = {'name': 'Carol', 'sex': 'female', 'age': 55}
    with open('name.json', 'w') as file:
        json.dump(names, file)


def read_json():
    with open('name.json', 'r') as file:
        data = json.load(file)
        print(data)


save_json()
read_json()
