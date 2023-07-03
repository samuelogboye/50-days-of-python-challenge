#!/usr/bin/python3

def my_discount():
    price = int(input("Enter the price of the product: "))
    discount = int(input("Enter the discount(percentage) of the product: "))
    return price - (price*(discount/100))


print(my_discount())
