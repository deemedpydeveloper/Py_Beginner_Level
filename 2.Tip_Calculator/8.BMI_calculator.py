# BMI Calculator.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# type checking.
print(type(height))  # both of them result in strings.
print(type(weight))
# calculate bmi by type conversion.
bmi = float(weight) / float(height) ** 2  # user can enter decimal values.
print(int(bmi))   # only integer value is printed out.