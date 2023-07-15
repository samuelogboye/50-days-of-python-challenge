#!/usr/bin/python3

def sort_length(strings):
    for i in range(len(strings)):
        min_index = i
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < len(strings[min_index]):
                min_index = j
        strings[i], strings[min_index] = strings[min_index], strings[i]
    return strings


a = ["Peter", "Jon", "Andrew"]
print(sort_length(a))
