#!/usr/bin/python3


while True:
    num1 = int(input("Enter the first number: "))
    print("Pick an operation you wanna perform")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")
    operator = input("Pick an operation you wanna perform: ")
    num2 = int(input("Enter the second number: "))

    operation = {
        1: num1 + num2,
        2: num1 - num2,
        3: num1 / num2 if num2 != 0 else "You cant divide by zero",
        4: num1 * num2}
    result = operation.get(int(operator), "Invalid Choice")
    print(result)
    choice = input("Do you wish to continue? Yes/y or No/n: ")
    choice_array = ["No", "N", "no", "n"]
    if choice in choice_array:
        print("Thanks for using this simple calculator")
        break
