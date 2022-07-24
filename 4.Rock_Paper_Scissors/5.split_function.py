# Split Method.

## It is used to separate the strings by reference.
## conversion from string to list is done.

family_names = input("Enter your family names with one space.\n")
family_list = family_names.split(" ")  # split method by space.
print(type(family_list))   # type checking.
print(family_list)  # prints a list.
