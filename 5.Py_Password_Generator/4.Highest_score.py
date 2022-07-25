# Calculate Highest score in the class.

# prompt from user.
student_scores = input("Input a list of students scores: ").split(" ")

# type conversion.
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# calculate max score.
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

# print max score.
print(f"The highest score in the class is: {max_score}")