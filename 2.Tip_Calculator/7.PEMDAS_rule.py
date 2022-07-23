# PEMDAS Rule.

# (), **, * or /, + or -.
# 👆 order of execution when any of them are on same line of code.
# left to right execution takes place.
# (3 * 3) = 9 and (3 / 3) = 1 then, (9 + 1.0 - 3).
# (9 + 1.0) = 10.0 then, (10.0 - 3) = 7.0. ----> Final answer.
print(3 * 3 + 3 / 3 - 3)
# Another example ----> Final answer is 3.0
print(3 * (3 + 3) / 3 - 3)