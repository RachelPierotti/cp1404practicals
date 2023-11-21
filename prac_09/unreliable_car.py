"""Unreliable Car class"""
from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, reliability, **kwargs):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive the car if reliable."""
        random_number = uniform(0, 100)
        if random_number >= self.reliability:
            distance = 0
        else:
            distance = distance
        distance_driven = super().drive(distance)
        return distance_driven
