#!/usr/bin/python3

import json


def save_json():
    names = {'name': 'Carol','sex': 'female','age': 55}
    with open('data.json', 'w') as file:
        json.dump(data, file)


save_json()
