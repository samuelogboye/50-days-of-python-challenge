#!/usr/bin/python3


def make_tuples(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError("Lists must be of equal length.")

    combined_list = []
    for i in range(len(list_a)):
        combined_list.append((list_a[i], list_b[i]))

    return combined_list


# Test the function
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
result = make_tuples(list_a, list_b)
print(result)  # Output: [(1, 5), (2, 6), (3, 7), (4, 8)]
