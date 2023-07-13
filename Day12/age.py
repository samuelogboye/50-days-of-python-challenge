#!/usr/bin/python3

import datetime


def age_in_minutes():
    current_year = datetime.datetime.now().year
    minutes = 0
    while (1):
        year_of_birth = input("Whats your year of birth?(4 digits): ")
        if len(year_of_birth) != 4 or not year_of_birth.isdigit():
            print("Invalid input. Enter a four-digit year using only digits.")
            continue

        year_of_birth = int(year_of_birth)
        if year_of_birth < 1900 or year_of_birth > current_year:
            print("Invalid input. Please enter a valid year.")
        else:
            minutes += ((current_year - year_of_birth)*365*24*60)
            break
    print("Your age in minutes is:", minutes)


age_in_minutes()
