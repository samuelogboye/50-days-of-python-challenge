#!/usr/bin/python3

def even_or_average():
    print("Enter 5 numbers")
    new_list = []
    even = []
    for i in range(1, 6):
        a = int(input("Enter Number {}: ".format(i)))
        new_list.append(a)

    for j in new_list:
        if j % 2 == 0:
            even.append(j)

    largest_even = max(even) if even else None
    average = sum(new_list) / len(new_list)
    if largest_even is not None:
        return "Largest Even Number: " + str(largest_even)
    return "Average: " + str(average)


print(even_or_average())
