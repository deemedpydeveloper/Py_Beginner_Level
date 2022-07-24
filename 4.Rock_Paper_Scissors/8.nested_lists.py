# Nested Lists.

fruits = ['apple', 'mango', 'banana', 'orange', 'pine-apple']
vegetables = ['carrot', 'cucumber', 'cabbage', 'spinach']
eatables = [fruits, vegetables]  # nesting lists inside an empty list.
print(eatables)  # prints two lists in one list.

## Accessing items of a nested list.

print(eatables[0][1])  # taps into eatables list and then to fruits list and picks 2nd item.