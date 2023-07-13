#!/usr/bin/python3


def your_vat():
    while True:
        try:
            item_price = int(input("Enter the price of the item: "))
            vat = int(input("Enter the VAT (VAT should be a percentage): "))
        except ValueError as e:
            print(e)
            continue

        try:
            total_price = item_price + (item_price * (vat / 100))
        except ZeroDivisionError:
            print("Error: VAT cannot be 0.")
            continue

        print("The total price for this item is {:.2f}".format(total_price))
        break  # Exit the loop after displaying the result


your_vat()
