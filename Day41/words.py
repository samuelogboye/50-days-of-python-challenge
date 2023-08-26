#!/usr/bin/python3


def words_with_vowels(a_string):
    final_list = []
    vowels = 'aeiou'

    splitted_string = a_string.split()
    for word in splitted_string:
        for letter in word:
            if letter in vowels:
                if word not in final_list:
                    final_list.append(word)

    return final_list


a = "You have no rhythm"
print(words_with_vowels(a))
