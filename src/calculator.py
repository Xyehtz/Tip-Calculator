# Obtain the total amount of the receipt 

total_amount = float(input("Enter the total amount of the receipt: "))

# Obtain the total percentage of the tip

tip_percentage = float(input("Enter the percentage of the tip: "))

# Calculate the amount of the tip

tip = (total_amount * tip_percentage) / 100

# Calculate the total amount to pay

pay_amount = total_amount + tip

print(f"Total amount of the receipt: {total_amount}")
print(f"Tip: {tip}")
print(f"Total amount to pay: {pay_amount}")