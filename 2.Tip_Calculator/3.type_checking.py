# Type Checking.

num_char = len(input("What is your name? "))
# print("your name has " + num_char + " characters") ----> TypeError : Since num_char is an integer and all the other are strings.
# So, if you rae not sure of what is the data type of a variable, use this method.

# type()  ---->  returns type of object placed inside parentheses.
print(type(num_char))  