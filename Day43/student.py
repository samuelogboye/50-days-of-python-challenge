#!/usr/bin/python3


def students_marks():
    score_dict = {}
    while True:
        name = input("Enter the name of the student: ")
        score = int(input("Enter {}'s score: ".format(name)))
        score_dict.update({name: score})
        print("{}'s score {} successfully stored".format(name, score))
        choice = input("Do you want to add more records? yes/no: ")
        if choice.lower() == "no":
            return score_dict


print(students_marks())
