#!/usr/bin/python3


import string


def analyse_string(a_string):
    """A function that returns the number of special characters
    words and total characters excluding whitespaces
    returned in a dictionary format"""

    special_character = 0

    """store all the punctuations in a variable using string module"""
    all_punctuation = string.punctuation

    """remove all whitespaces"""
    a_string = a_string.replace(" ", "")

    string_length = len(a_string)

    for char in a_string:
        if char in all_punctuation:
            special_character += 1

    word_length = string_length - special_character

    dict_char = {"special character": special_character, "words": word_length,
                 "total characters": string_length}

    return dict_char


a = 'Python has a string format operator %. This functions\
analogously to printf format strings in C, e.g. "spam=%s\
eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2'

print(analyse_string(a))
