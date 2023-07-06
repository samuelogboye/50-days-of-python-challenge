#!/usr/bin/python3


def prime_numbers():
    """A function that list all the prime numbers
    from one to a number gotten from user"""
    num = int(input("Enter a number: "))
    prime = []
    for i in range(2, num+1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    print(prime)


prime_numbers()
