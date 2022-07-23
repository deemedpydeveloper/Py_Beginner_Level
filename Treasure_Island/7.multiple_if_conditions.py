# Multiple If Statements.

print("Welcome to the 'Roller Coaster'.")
height = int(input("What is your height? "))
bill = 0
if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 3
        print(f"Child fare is: ${bill}.")
    elif age <= 19:
        bill = 7
        print(f"Adult fare is: ${bill}.")
    elif age <= 60:
        bill = 10
        print(f"fare is: ${bill}.")
    else:
        bill = 12
        print(f"fare is: ${bill}.")
    photo_needed = input("Do you want a photo? Type 'yes' or 'no'. ")
    if photo_needed == 'yes':
        bill += 3
    print(f"Your final bill is: ${bill}.")
else:
    print("You are not eligible for this ride.")