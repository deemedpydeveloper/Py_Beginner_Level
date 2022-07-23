# Checking the given number whether it is Odd or Even.

number = int(input("Which number do you want to check? "))
# checks if number when divide by 2, gives remainder 0(zero) or not.
if number % 2 == 0:  # If it evaluates to be true then, executes this statement.
    print("This is an even number.")
else:  # else this statement.
    print("This is an odd number.")