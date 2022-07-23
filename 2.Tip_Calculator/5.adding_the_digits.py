# Adding the two digits of an input number.

two_digit_number = input("Type a two digit number: ")
# type checking.
print(type(two_digit_number))
# subscripting.
first_char = two_digit_number[0]
print(first_char)  # checking index value.
second_char = two_digit_number[1]
print(second_char)  # checking index value.
# type conversion.
fist_digit = int(first_char)
second_digit = int(second_char)
sum = fist_digit + second_digit
print(sum)