#!/usr/bin/python3


def average_calories():
    new = []
    count = 0
    print("Welcome to Average Calories Calculator")
    days = int(input("How many days do you want to lodge: "))
    for i in range(1, 20):
        num = input("Day {}: ".format(i))
        if num == 'done':
            break
        new.append(int(num))
        count += 1

    return "Your average calories intake over" + str(count) + "days is" + str(sum(new)/count)


print(average_calories())
