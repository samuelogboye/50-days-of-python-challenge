#!/usr/bin/python3

def translate(a_string):
    new_string = ''
    vowel = 'aeiou'
    a_string = a_string.lower().split()

    for word in a_string:
        if word[0] in vowel:
            word += 'yay'
        else:
            word = word[1:] + word[0] + 'ay'
        new_string += ' ' + word
    return new_string.strip()


a = 'i love pythoN'
print(translate(a))
