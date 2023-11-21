"""Program to test UnreliableCar class"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Run test on new class type."""
    my_car = UnreliableCar("my_car", 100, 70)
    print(my_car)
    fail_count = 0
    success_count = 0
    for i in range(0, 100):
        UnreliableCar.drive(my_car, 50)
        if my_car.odometer == 0:
            fail_count += 1
            print("Car didn't work :(")
        else:
            success_count += 1
            print("Car drove!")
        my_car.odometer = 0
        my_car.fuel = 100
    print(f"Fails:{fail_count}, Successes:{success_count}")


main()
