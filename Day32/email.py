#!/usr/bin/python3

import re


def is_valid(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))


def email_validator(a_list):
    if a_list == []:
        return "all emails are invalid"
    valid_emails = []
    for word in a_list:
        if is_valid(word):
            valid_emails.append(word)
    return valid_emails


emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
print(email_validator(emails))
