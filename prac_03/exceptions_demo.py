"""
CP1404 - Prac 3
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Please enter a non-zero integer!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1: A ValueError will occur when a non-integer number is entered, or other symbol e.g. "a" is entered.
# Q2: A ZeroDivisionError will occur when the denominator is entered as zero.
# Q3: Add a loop so that if zero is the denominator input, the program asks the user for a different value before
# evaluating the fraction.
