# List Data Structure.

## Data Structure ---> A Systematic way of organizing data.
## 'List' is one type of data structure.
## Unlike Variables which stores only one value, lists store multiple data types.
## 'Order' of items stored in lists does matter always.

integers = [1, 2, 3, 4, 5]   # list initialization.
float_num = []   # list declaration.

## List can store various data types.

data_types = [1, 2.3, 'tejendra']

## Each item of a list can be accessed by indexing.

# Positive indexing.
print(data_types[0])   # prints the starting value of a list.

# negative indexing.
print(data_types[-1])

## changing the value.

data_types[1] = 2.4
print(data_types)

## Appending new item to the list.

data_types.append('yerra')   # appends only one item at the end of the list.
print(data_types)

## Adding multiple items to the list.

data_types.extend([2, 6.5, 'Python'])   # extends the list by adding multiple items at the end.
print(data_types)