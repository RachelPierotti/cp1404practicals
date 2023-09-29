"""
CP1404 Practical 1
Calculate price of shopping cart with multiple items + discount
"""

total_price = 0
discount_rate = 0.1
number_of_items = int(input("Enter number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))
for i in range(0, number_of_items):
    item_price = float(input("Enter item price: $"))
    total_price += item_price
if total_price > 100:
    total_price_including_discount = float(total_price * (1 - discount_rate))
    print(f"Total price for {number_of_items} items is ${total_price_including_discount:.2f} (including discount)")
else:
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
