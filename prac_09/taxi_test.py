"""taxi_test program"""
from prac_09.taxi import Taxi


def main():
    """Create a new taxi object and drive it"""
    my_taxi = Taxi("Prius 1", 100)
    Taxi.start_fare(my_taxi)
    Taxi.drive(my_taxi, 40)
    fare = Taxi.get_fare(my_taxi)
    print(f"Taxi's details: {my_taxi}")
    print(f"Current fare is: ${fare:.2f}")
    Taxi.start_fare(my_taxi)
    Taxi.drive(my_taxi, 100)
    fare = Taxi.get_fare(my_taxi)
    print(f"Taxi's details: {my_taxi}")
    print(f"Current fare is: ${fare:.2f}")
    # because of the nature of Car class, taxi stops driving after
    # 60km as it runs out of fuel, so distance and fare is impacted
    # by this attribute


main()
