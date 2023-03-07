# Day 14 -> Higher or Lower Game
from data import data
from random import randint
import art

GAME_SCORE = {'score': 0}

RESET = False
FIRST_PLAY = True
IS_RUNNING = True
GAME_OVER = False
ANSWERED = False


def display_game(numbers):
    """Displays game questions using random selection in numbers[a, b] as index"""

    text1_length = 12 + len(data[numbers[0]]['name']) + len(data[numbers[0]]['description']) + len(
        data[numbers[0]]['country'])

    if data[numbers[0]]['description'][0].lower() == 'a':
        text1_length += 1

    text2_length = 12 + len(data[numbers[1]]['name']) + len(data[numbers[1]]['description']) + len(
        data[numbers[1]]['country'])

    if data[numbers[1]]['description'][0].lower() == 'a':
        text2_length += 1

    print(art.logo)

    if message != '':
        print(message, GAME_SCORE['score'])

    print(" " * 11 + "┌" + "─" * text1_length + "┐")

    print("Compare A: │ " + data[numbers[0]]['name'] + ", ", end="")

    if data[numbers[0]]['description'][0].lower() == 'a':
        print("an ", end="")
    else:
        print("a ", end="")

    print(data[numbers[0]]['description'].lower() + f" from {data[numbers[0]]['country']}" + " │")

    print(" " * 11 + "└" + "─" * text1_length + "┘")

    print(art.vs)

    print(" " * 11 + "┌" + "─" * text2_length + "┐")

    print("Against B: │ " + data[numbers[1]]['name'] + ", ", end="")

    if data[numbers[1]]['description'][0].lower() == 'a':
        print("an ", end="")
    else:
        print("a ", end="")

    print(data[numbers[1]]['description'].lower() + f" from {data[numbers[1]]['country']}" + " │")

    print(" " * 11 + "└" + "─" * text2_length + "┘")


def check_input(choice, numbers):
    if data[numbers[0]]['follower_count'] > data[numbers[1]]['follower_count']:

        return choice == 'a'

    else:

        return choice == 'b'


def final_comparison(choice, numbers):
    result = data[numbers[0]]['follower_count'] > data[numbers[1]]['follower_count']

    if result:
        print(f"You chose [{choice.upper()}]. " + data[numbers[0]]['name'] + " has " + str(
            data[numbers[0]]['follower_count']) + " million followers, " + str(
            (round(data[numbers[0]]['follower_count'] - data[numbers[1]]['follower_count']))) + " million more than " +
              data[numbers[1]]['name'])
    else:
        print(f"You chose [{choice.upper()}]. " + data[numbers[1]]['name'] + " has " + str(
            data[numbers[1]]['follower_count']) + " million followers, " + str(
            round((data[numbers[1]]['follower_count'] - data[numbers[0]]['follower_count']))) + " million more than " +
              data[numbers[0]]['name'])


dataframe_length = len(data)

number2 = randint(0, (dataframe_length - 1))
message = ''

while IS_RUNNING:

    MESSAGES = ["Correct! Current score:", "Sorry, that's wrong! Final score:"]

    ANSWERED = False

    if RESET:
        message = ''
        number2 = randint(0, (dataframe_length - 1))
        RESET = False

    if FIRST_PLAY:

        print(art.logo)

        player_input = input(
            "\nWelcome to Higher Lower, would you like to play a game?\n('q' = exit, press any key to continue)\n> ").lower()
        if player_input == 'q':
            IS_RUNNING = False
            break
        else:
            FIRST_PLAY = False
            continue

    newNumber = False
    temp = None

    numbers = []

    number1 = number2
    number2 = 0

    while not newNumber:

        temp = randint(0, (dataframe_length - 1))

        if temp == number1:
            continue

        else:
            number2 = temp
            newNumber = True
    else:
        numbers = [number1, number2]

    while not ANSWERED and not GAME_OVER:

        display_game(numbers)

        player_input = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if player_input == 'q':
            GAME_OVER = True
            IS_RUNNING = False
            break

        elif player_input == 'a':
            ANSWERED = True
            if check_input(player_input, numbers):
                GAME_SCORE['score'] += 1
                message = MESSAGES[0]
            else:
                message = MESSAGES[1]
                GAME_OVER = True
            continue

        elif player_input == 'b':
            ANSWERED = True
            if check_input(player_input, numbers):
                GAME_SCORE['score'] += 1
                message = MESSAGES[0]
            else:
                message = MESSAGES[1]
                GAME_OVER = True
            continue

        else:
            message = "Invalid input. Please enter 'A' or 'B'"
            continue

    if GAME_OVER:
        display_game(numbers)
        final_comparison(player_input, numbers)
        print()

        player_input = input("Would you like to play again?\n('q' = exit, press any key to continue)\n\n> ").lower()

        if player_input == 'q':
            IS_RUNNING = False
            break
        else:
            RESET = True
            GAME_SCORE['score'] = 0
            GAME_OVER = False
            continue
