print("Welcome to the tip calculator!")
bill_on_receipt = float(input("What was the total bill? $"))
tip_percentage = float(input("How much percent would you like to tip? "))
people_splitting = int(input("How many people to split the bill? "))

tip_decimal = tip_percentage / 100
bill_with_tip = bill_on_receipt * (1 + (tip_decimal))
bill_split = bill_with_tip / people_splitting

print(f"Each person should pay: ${bill_split:.2f}")