#!/usr/bin/python3


def count_the_vowels(a_string):
    vowels = "aeiou"
    count = 0
    vowel_set = set()
    for letter in a_string.lower():
        if letter in vowels:
            vowel_set.add(letter)
    return len(vowel_set)


print(count_the_vowels("hello"))
print(count_the_vowels("saas"))
