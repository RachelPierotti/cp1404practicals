"""Unreliable Car class"""
from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, reliability:{self.reliability}%"

    def drive(self, distance):
        """Drive the car if reliable."""
        random_number = uniform(0, 100)
        if random_number >= self.reliability:
            distance = 0
        else:
            distance = distance
        distance_driven = super().drive(distance)
        return distance_driven
