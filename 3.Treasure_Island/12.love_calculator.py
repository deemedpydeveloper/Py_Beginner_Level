# Love Calculator.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")   # \n --> to point cursor in new line.
name1.lower()  # this is correct.
name2 = input("What is their name? \n").lower()  # this is simplified version.
total_name = name1 + name2
t = total_name.count('t')
r = total_name.count('r')
u = total_name.count('u')
e = total_name.count('e')
true = str(t + r + u + e)
l = total_name.count('l')
o = total_name.count('o')
v = total_name.count('v')
_e = total_name.count('e')
love = str(l + o + v + _e)   # for concatenation.
true_love = true + love
love_score = int(true_love)   # for comparision & printing out.
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")