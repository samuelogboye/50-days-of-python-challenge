#!/usr/bin/python3

from textblob import TextBlob


def spelling_checker():
    while True:
        text = input("Enter a word: ")
        blob = TextBlob(text)

        corrected_blob = blob.correct()
        if corrected_blob.lower() == text.lower():
            return corrected_blob
        else:
            choice = input("Do you want to type {}? yes/no: ".format(corrected_blob))
            if choice.lower() == "yes":
                return corrected_blob
            elif choice.lower() == "no":
                print("Please enter the word again.")
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


print(spelling_checker())
