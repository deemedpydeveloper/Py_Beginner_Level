# Check whether the given year is leap year or not.

# taking input.
year = int(input("Which year do you want to check? "))
# checking conditions.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")