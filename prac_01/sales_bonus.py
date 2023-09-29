"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.1
        calculate_bonus = sales * bonus_rate
        print(f"Bonus: ${calculate_bonus:.2f}")
    elif sales >= 1000:
        bonus_rate = 0.15
        calculate_bonus = sales * bonus_rate
        print(f"Bonus: ${calculate_bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Invalid option")
