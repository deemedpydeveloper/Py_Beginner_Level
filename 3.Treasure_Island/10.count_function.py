# Count Function.

## .count(item, start, end) ---> it returns the number of times a specified value appears in a string or a list.
## value ---> is the argument passed to which count is to be determined.
## start , end ---> these are the index values of substrings or list items for counting.(default start = 0 and end = last index value.)
name = 'Tejendra'  # each character in a sting is called a 'substring'.
print(name.count('T'))
print(name.count('t'))  # cas-sensitive.