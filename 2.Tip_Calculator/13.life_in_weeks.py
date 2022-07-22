# Calculate the number of weeks in life.

# type conversion.
age = int(input("What is your current age? "))

# Setting the limit to 90 years.
years_left = 90 - age

# calculating days, weeks and months left.
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# printing it out using an f-String.
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")