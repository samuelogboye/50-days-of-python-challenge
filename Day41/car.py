#!/usr/bin/python3


class Ford:

    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print("car_model = {}".format(self.model))
        print("Color = {}".format(self.color))
        print("Year = {}".format(self.year))
        print("Transmission = {}".format(self.transmission))
        print("Electric = {}".format(self.electric))


class BMW(Ford):
    pass


class Tesla(Ford):
    pass


bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = Tesla("S", "beige", 2017, "Auto", True)
ford1 = Ford("focus", "white", 2020, "Auto", False)


ford1.print_cars()
