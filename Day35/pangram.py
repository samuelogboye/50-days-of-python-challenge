#!/usr/bin/python3


def check_pangram(a_string):
    alphabet = 'abcdefghijklmnopqrstwxyz'
    for letter in alphabet:
        if letter not in a_string.lower():
            return False
        return True


a = 'the quick brown fox jumps over a lazy dog'
print(check_pangram(a))
