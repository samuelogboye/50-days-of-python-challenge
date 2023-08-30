#!/usr/bin/python3

import json


def save_json():
    names = {'name': 'Carol', 'sex': 'female', 'age': 55}
    with open('name.json', 'w', newline="") as file:
        json.dump(names, file)


save_json()
