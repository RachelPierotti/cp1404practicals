"""Program to check SilverServiceTaxi class works correctly"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Create a new taxi object and drive it"""
    my_taxi = SilverServiceTaxi("Porsche", 100, 2)
    SilverServiceTaxi.start_fare(my_taxi)
    SilverServiceTaxi.drive(my_taxi, 18)
    print(f"Fare: ${SilverServiceTaxi.get_fare(my_taxi):.2f}")
    print(f"Taxi's details: {my_taxi}")


main()
