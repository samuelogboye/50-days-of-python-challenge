#!/usr/bin/python3


def average_calories():
    new = []
    count = 0
    print("Welcome to Average Calories Calculator")
    print("Lodge in according to date, when done type 'done'")
    for i in range(1, 20):
        num = input("Day {}: ".format(i))
        if num == 'done':
            break

        new.append(int(num))
        count += 1
        average = round(sum(new)/count, 2)
    return "Your average calories intake over " + str(count) + " days is " + str(average)


print(average_calories())
