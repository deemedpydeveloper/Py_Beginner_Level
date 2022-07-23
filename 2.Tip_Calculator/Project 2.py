# Tip Calculator.

print("Welcome to the tip calculator.")

# type conversion.
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_number = int(input("How many people to split the bill? "))

# Calculation for each person.
total_bill += total_bill * (tip_percentage / 100)   # Short-hand notation.
final_bill = format(total_bill / split_number, '.2f')  # Format function.

# f-String.
print(f"Each person should pay: ${final_bill}")