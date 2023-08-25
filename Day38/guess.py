#!/usr/bin/python3
import random


def guess_a_number():
    """A function that ask user to guess a ramdonly generated number
    if the user guesses a higher number,
        the code should say the guess is too high
    if the user guesses a lower number,
        the code should say the guess is too low
    the user should get a maximum of 3 guesses
    when the user guesses rightm the code should declare the user the winner
    after 3 guesses, the code should declare the user the loser
    """
    random_number = random.randint(1, 10)
    guess_count = 0
    while guess_count < 3:
        print("You have {} guesses left".format(3 - guess_count))
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1
        if guess == random_number:
            print("You win!")
            break
        elif guess > random_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    else:
        print("You lose!")


guess_a_number()
