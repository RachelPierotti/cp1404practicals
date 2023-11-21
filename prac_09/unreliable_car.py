"""Unreliable Car class"""
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, reliability, **kwargs):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability
