row1 = ["📦", "📦", "📦"]
row2 = ["📦", "📦", "📦"]
row3 = ["📦", "📦", "📦"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# type conversion.

index_1 = int(position[0])  # column number.
index_2 = int(position[1])  # row number.

# item index in list index.

column_num = index_1 - 1
row_num = index_2 - 1

# replacing item in list.

map[row_num][column_num] = '🪙'  # taps into nested list.
print(f"{row1}\n{row2}\n{row3}")