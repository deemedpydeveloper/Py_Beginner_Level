# Calculate Average Heights of Students.

student_heights = input("Input a list of student heights: ").split(" ")  # for converting the entries into a list.
for n in range(0, len(student_heights)):  # for loop to store student heights as integers.
    student_heights[n] = int(student_heights[n])   # type conversion and adding it to the list.
print(student_heights)  # a list.
total_height = 0
total_students = 0
for height in student_heights:   # use of for loop fpr calculating average.
    total_students += 1   # for calculating number of students.
    total_height += height  # for calculating the sum of all student heights.
print(total_height)   # total of heights of all students.
print(total_students)  # total number of students.
avg = round(total_height / total_students)   # calculating average.
print(avg)  # prints average.