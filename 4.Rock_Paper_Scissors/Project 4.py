# Rock-Paper-Scissor.

## ascii art.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

guesses = [rock, paper, scissor]
player_choose = int(input('Type "0" for rock, "1" for paper or "2" for scissors.\n'))
import random
computer_choose = random.choice(guesses)  # randomization.
if player_choose > 2:
    print('Invalid Choice, You Lose')
else:
    if player_choose == 0 or 1 or 2:
        print(f'Player Choose:\n{guesses[player_choose]}')  # displaying figures.
        print(f'Computer Choose:\n{computer_choose}')

        # comparision.

        if player_choose == 0:
            if computer_choose == scissor:
                print('You win')
            elif computer_choose == rock:
                print('Draw')
            else:
                print('You Lose')
        elif player_choose == 1:
            if computer_choose == rock:
                print('You Win')
            elif computer_choose == paper:
                print('Draw')
            else:
                print('You Lose')
        else:
            if computer_choose == paper:
                print('You Win')
            elif computer_choose == scissor:
                print('Draw')
            else:
                print('You Lose')