# Switch the variable values.

a = input("a: ")
b = input("b: ")
c = a  # creating a variable to alter the values of a and b.
a = b
b = c
print("a = " + a)
print("b = " + b)