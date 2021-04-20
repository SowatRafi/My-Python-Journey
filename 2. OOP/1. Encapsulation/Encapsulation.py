class Cars:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


def Printing(car=None, speed=None, colour=None):
    if car is None:
        if colour is None:
            print("\nYour car has no colour?")
        if speed is None:
            print("\nNo speed has been initialized.")
        print("\nPlease give the brand name.")
    else:
        print(f"\nThe {car} car's top speed is {speed} per hour.")
        print(f"The {car}'s colour is {colour}")


BMW = Cars(250, "Silver")
Toyota = Cars(150, "White")
mercedes_benz = Cars(231, "Grey")

# Changing the values
BMW.set_speed(304)
BMW.set_color("Black")
BMW.speed = 500  # Completely ignored this line because of the private variables
BMW.color = 2134678  # Completely ignored this line because of the private variables


Printing("BMW", BMW.get_speed(), BMW.get_color())
Printing("Toyota", Toyota.get_speed(), Toyota.get_color())
Printing("Mercedes-Benz", mercedes_benz.get_speed(), mercedes_benz.get_color())

Printing()
