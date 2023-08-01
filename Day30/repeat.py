#!/usr/bin/python3


def repeated_name(a_list):
    name_counts = {}
    for name in a_list:
        name_counts[name] = name_counts.get(name, 0) + 1
    most_occurrences = max(name_counts, key=name_counts.get)
    return most_occurrences


names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(names))
