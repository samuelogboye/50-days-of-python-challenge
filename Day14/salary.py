#!/usr/bin/python3

def your_salary():
    teachers_name = input("Enter the teacher's name: ")
    periods = int(input("Enter the number of periods: "))
    rate = 20
    if periods > 100:
        overtime = periods - 100
        salary = (100*rate) + (overtime*25)
    else:
        salary = periods*rate
    print()
    print("Teacher: ", teachers_name)
    print("Periods: ", periods)
    print("Gross salary: ", salary)


your_salary()
