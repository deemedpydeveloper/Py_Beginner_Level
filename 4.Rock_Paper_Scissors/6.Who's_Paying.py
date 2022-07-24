# Who's Paying.

names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")  # string to list conversion.
import random   # random module.
# len(names) - 1 ---> IndexError can be avoided, since indexing starts from '0'.
rand_index = random.randint(0, len(names) - 1)  # randomization of index.
print(f"{names[rand_index]} is going to buy the meal today.")   # printing list[index].