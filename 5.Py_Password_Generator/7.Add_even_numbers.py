# Addition of even numbers between 1 - 100.

total1 = 0

# with step method.
for number in range(0, 101, 2):
    total1 += number
print(total1)

total2 = 0
# without step method.
for number in range(0, 101):
    if number % 2 == 0:
        total2 += number
print(total2)