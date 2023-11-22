"""SilverServiceTaxi class."""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi that includes fanciness factor"""
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class
        Taxi (which inherits from its parent class Car)."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like Taxi with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (self.price_per_km * self.current_fare_distance) + self.flagfall
