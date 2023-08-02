#!/usr/bin/python3

def longest_word(a_list):
    new_list = []
    longest = ""
    for word in a_list:
        if len(word) > len(longest):
            longest = word
    new_list.append(len(longest))
    new_list.append(longest)
    return new_list


a = ['Java', 'JavaScript', 'Python']
print(longest_word(a))
