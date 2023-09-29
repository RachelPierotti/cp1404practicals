"""
CP1404 Practical 1, Extension
"""

x_value = int(input("Enter x value: "))
y_value = int(input("Enter y value: "))
menu = ("1 = Show the even numbers from x to y "
        "\n2 = Show the odd numbers from x to y "
        "\n3 = Show the squares of the numbers from x to y "
        "\n4 = Exit the program")
print(menu)
choice = int(input("Enter option from menu: "))
while choice != 4:
    if choice == 1:
        if (x_value % 2) != 0:
            for i in range(x_value + 1, y_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(x_value, y_value + 1, 2):
                print(i, end=' ')
    elif choice == 2:
        if (x_value % 2) == 0:
            for i in range(x_value + 1, y_value + 1, 2):
                print(i, end=' ')
        else:
            for i in range(x_value, y_value + 1, 2):
                print(i, end=' ')
    elif choice == 3:
        for i in range(x_value, y_value + 1):
            print(i * i, end=' ')
    else:
        print("Invalid input")
    choice = int(input("Enter option from menu: "))
print("Program ended.")