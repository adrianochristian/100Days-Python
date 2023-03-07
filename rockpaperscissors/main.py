# Day 4 -> Randomisation and Python Lists
# Rock Papers and Scissors
import random

options = ['Rock', 'Paper', 'Scissors']
player = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. "))
if options[player]:
    print(options[player])
else:
    print('Choose a number between 0 and 2 next time. You lost')
    exit()

print("Computer chose: ")
computer = random.randint(0, 2)
print(options[computer])

if computer == player:
    print('Draw')
elif computer == 0 and player == 2:
    print('You Lose')
elif player == 0 and computer == 2:
    print('You win')
elif computer > player:
    print('You lose')
elif player > computer:
    print('You Win')
