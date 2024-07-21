# Creating Simple Classes:
# Write a Python class named Car with attributes like model, color, and year.
# Create an object of the Car class with specific values for its attributes.
# Write a method in the Car class called accelerate() that simply prints "Accelerating...".


class Car:
    model="bugati"
    color="yellow"
    year=2022
    def accelerate(self):
        print("Accelerating...")

a=Car()
a.accelerate()