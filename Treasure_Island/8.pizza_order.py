# Pizza Order.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == 'S':
    bill = 15
    print(f"Small Pizza: ${bill}.")
    if add_pepperoni == 'Y':
        print(f"Pepperoni for Small Pizza: +$2.")
        bill += 2
elif size == 'M':
    bill = 20
    print(f"Medium Pizza: ${bill}.")
    if add_pepperoni == 'Y':
        bill += 3
        print("Pepperoni for Medium Pizza: +$3.")
else:
    bill = 25
    print(f"Large Pizza: ${bill}.")
    if add_pepperoni == 'Y':
        bill += 3
        print("Pepperoni for Large Pizza: +$3.")
if extra_cheese == 'Y':
    bill += 1
    print("Extra cheese for any pizza: +$1.")
print(f"Your final bill is: ${bill}.") 