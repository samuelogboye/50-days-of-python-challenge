#!/usr/bin/python3


import emoji


def python_snakes(num):
    snake_emoji = '🐍'
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(snake_emoji * num)
        else:
            print(snake_emoji + ' ' * (num - 2) + snake_emoji)


# Example usage
num = int(input("What number of snake do you wanna make?: "))
python_snakes(num)
