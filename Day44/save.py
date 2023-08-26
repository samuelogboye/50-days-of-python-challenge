#!/usr/bin/python3

import csv


def save_emails():
    emails_store = []
    while True:
        print("Enter email address you wanna store")
        print("Once done, type 'done' instead of email address to save it")
        emails = input("Enter an email address ")

        if emails.lower() == "done":
            break
        emails_store.append(emails)

    with open("emails.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(emails_store)


def open_emails():
    with open("emails.csv", mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

        for row in data:
            for word in row:
                print(word)


save_emails()
open_emails()
