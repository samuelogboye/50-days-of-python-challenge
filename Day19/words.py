#!/usr/bin/python3

def count_words(word):
    sum = 0
    for i in word.split():
        sum += 1
    return sum


def count_elements(words):
    sum = 0
    for i in words.replace(" ", ""):
        sum += 1
    return sum


a = "I love learning"
print(count_words(a))
print(count_elements(a))
