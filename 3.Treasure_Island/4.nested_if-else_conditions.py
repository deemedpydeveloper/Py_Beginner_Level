# Nested If -else Statements.
print("Welcome to the 'Roller Coaster'.")
# type conversion.
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You are eligible for ride.")
    # type conversion.
    age = int(input("What is your age? "))
    if age <= 12:
        print("Pay 5$")
    # elif statement ---> used to check multiple conditions.
    elif age <= 18:
        print("Pay 7$")
    else:
        print("Pay 10$")
else:
    print("You are not eligible for ride.")