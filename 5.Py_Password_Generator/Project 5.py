# Py Password Generator.

## shortcut for creating a list of alphabets.
# LETTERS = input("Enter letters: ").split(" ")
# print(LETTERS)

# creating lists.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

# prompt from user.
print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# randomization 1.
password = []
for letter in range(1, nr_letters + 1):
    password += random.choice(letters)
for number in range(1, nr_numbers + 1):
    password += str(random.choice(numbers))
for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(password)

# randomization 2.
random.shuffle(password)
print(password)

# list to string conversion
final_password = ""
for char in password:
    final_password += char

# final password.
print(f"Your password is: {final_password}")