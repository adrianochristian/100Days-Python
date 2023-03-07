# Day 7 -> Hangman
import random
import hangman_art as art
from hangman_words import word_list

game_end = False
lives = 6

chosen_word = random.choice(word_list)
display_word = []

for char in chosen_word:
    display_word += "_"

print(art.logo)
print(f"{''.join(display_word)}")

while not game_end:
    guess = input('Guess a letter: ').lower()
    if guess in display_word:
        print(f"You've already guessed the letter {guess}")
    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if char == guess:
            display_word[position] = char

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, and that's a wrong letter. You lose a life")

    print(art.stages[lives])
    print(f"{''.join(display_word)}")

    if '_' not in display_word:
        game_end = True
        print("You win")
    elif lives == 0:
        game_end = True
        print("You lost")
