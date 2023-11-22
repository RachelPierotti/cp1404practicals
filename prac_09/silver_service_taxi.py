"""SilverServiceTaxi class."""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi includes fanciness factor"""
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class
        Taxi (which inherits from its parent class Car)."""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km *= fanciness

