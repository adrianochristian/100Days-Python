# Day 3 -> Working with logic and conditional operators
# Island Treasure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
# Game
print("Welcome to the Treasure Island Game.\nYour mission is to find the treasure")
path = input("You're at a crossroad. Where do you want to go? Left or Right? ").lower()
if path == 'left':
    path = input(
        "You come to a lake. There is a island in the middle of thte lake. Swim across or Wait for a boat? ").lower()
    if path == 'wait':
        path = input(
            "You arrive at the island, unharmed. There is a house with 3 doors. One Red, one Yellow and one Blue. "
            "Which do you choose? ").lower()
        if path == ('red' or 'blue'):
            print("You enter a room of beasts. Game Over")
        elif path == 'yellow':
            print("You won")
    elif path == 'swim':
        print("You drowned. Game Over")
elif path == 'right':
    print("You got killed by a grizzly bear. Game Over")
