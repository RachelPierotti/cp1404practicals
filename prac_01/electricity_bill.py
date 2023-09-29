"""
CP1404 - Prac 1, Practice Section
Electricity Bill Estimator
"""
# 1.
cents_per_kWh = float(input("Enter cents per kWh: "))
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

estimated_bill = number_of_billing_days * daily_use_in_kWh * cents_per_kWh / 100
print(f'Estimated bill: ${estimated_bill:.2f}')

# 2.
tariff = 0
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_type_number = int(input("Enter tariff type number (11 or 31): "))
print(tariff_type_number)

while tariff_type_number != 11 and tariff_type_number != 31:
    print("Invalid tariff type number")
    tariff_type_number = int(input("Enter tariff type number (11 or 31): "))
if tariff_type_number == 11:
    tariff = TARIFF_11
    print("Tariff", tariff)
else:
    tariff = TARIFF_31
    print("Tariff", tariff)
estimated_bill = estimated_bill * (1 + tariff)
print(f"Estimated bill: ${estimated_bill:.2f}")
