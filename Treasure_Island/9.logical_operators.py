# Logical Operators.

## and ---> if both satisfy the condition ,then only it returns 'True'.
## or ----> if either of them or both satisfy the condition, then it returns 'True'.
## not ---> reverses a condition.

### Example.

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
        print(f"Youth fare is: ${bill}.")
    elif age <= 45 and age <= 55:  # and logical operator.
        print("Adult fare is: $0.")
    else:
        bill = 10
        print(f"Aged fare is: ${bill}.")
    photo_needed = input("Do you want a photo? Type 'yes' or 'no'. ")
    if photo_needed == 'yes':
        bill += 3
    print(f"Your final bill is: ${bill}.")
else:
    print("You are not eligible for this ride.")