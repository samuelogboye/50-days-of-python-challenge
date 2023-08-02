#!/usr/bin/python3


def password_validator():
    while True:
        password = input("Enter a password: ")

        if len(password) < 8:
            print("Password should be at least 8 characters long.")
            continue

        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_number = any(char.isdigit() for char in password)

        if not has_uppercase:
            print("Password should have at least one uppercase letter")
            continue

        if not has_lowercase:
            print("Password should have at least one lowercase letter")
            continue

        if not has_number:
            print("Password should have at least one number")
            continue

        print("Valid password.")
        return password


valid_password = password_validator()
print("Valid password entered:", valid_password)
