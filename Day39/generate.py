#!/usr/bin/python3


import random
import string


def generate_password():
    """Password generator"""
    count = 0
    password = ''

    print("1. weak")
    print("2. Strong")
    print("3. Very Strong")
    try:
        how_strong = int(input("How strong do you want the password to be? "))
    except ValueError:
        return "Invalid Choice"

    while True:
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += str(random.randint(1, 9))
        password += random.choice(string.punctuation)
        count += 1
        if count == 12:
            break

    """convert the string to a list of charaters, then shuffle"""
    password_list = list(password)
    random.shuffle(password_list)

    """join the shuffled characters back to string"""
    shuffled_password = ''.join(password_list)

    """determine password lenght based on choice"""
    if how_strong == 1:
        return shuffled_password[:5]
    elif how_strong == 2:
        return shuffled_password[:8]
    elif how_strong == 3:
        return shuffled_password[:12]
    else:
        return "Error"


print(generate_password())
