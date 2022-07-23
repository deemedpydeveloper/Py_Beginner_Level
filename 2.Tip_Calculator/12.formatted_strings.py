# f-String.

# without using f- strings.
name = 'Tejendra'
weight = 75  # string
height = 1.75  # integer
print(type(height))  # float
# it is very tedious task to type convert and concatenate.
print("Your name is " + name + "," + "your weight is " + str(weight) + " " + "and your height is " + str(height) + ".")

# with usage of f-String.
# comparitively less task than in line 9.
print(f"Your name is {name},your weight is {weight} and your height is {height}.")